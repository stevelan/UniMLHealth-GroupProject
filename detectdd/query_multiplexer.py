# given a query parameterised by two parameters that have a one-to-many relationship and a multimap
# with keys of the "one" side of the relationship, and values of the "many" side, performs batches of queries
# so that only one-to-one relationships are queried. The query must SELECT the key value, and this will be used to
# resolve the query results against each tuple. Performs as max(count(value)) queries, which can be many orders of magnitude
# smaller than a linear approach.
from datetime import datetime
from string import Template

import pandas as pd


class WhereClauseGenerator:
    def __init__(self, where_fragment:str, key_col: str, val_col: str):
        self.key_col = key_col
        self.val_col = val_col
        self.where_fragment= Template(where_fragment)


    def generate(self, key_val_pairs: list):

        if len(key_val_pairs) == 0:
            raise Exception("Empty list of tuples passed in to generate")


        clause = ""
        for key_data, val_data in key_val_pairs:
            if clause != "":
                clause += " OR "
            clause +=  self.where_fragment.substitute({self.key_col : key_data, self.val_col: val_data})
        return clause




# We need to be able to generate data for each potential drug interaction event, represented by a (stay_id, dose_time)
# the cohort data that we have, can have multiple dose times for a given stay ID, we need to keep the data for these
# seperate. The multi plexer helps to avoid generating performing one query per tuple, and instead allows one query per
# set of unique stay ids. So if we have data:
#
# stay_id : 1, starttimes: [10, 11, 12],
# stay_id : 2, starttimes: [8, 9],
# stay_id : 3, startime: [7]
#
# We will get 3 queries:
# query 1: (1, 10), (2, 8), (3, 7)
# query 2: (1, 11), (2, 9)
# query 3: (1, 12)
#
# In this example, this reduces the number of queries executed from one per tuple (6) to 3, the max length of the
# starttimes of any one tuple.
#
# In practice this reduces the number of queries from 80,000 to 60, a thousand-fold reduction in queries.
class QueryMultiplexer:

    # requires an authenticated big query client
    def __init__(self, big_query_client):
        self.biq_query_client = big_query_client

    #
    #
    # parameters:
    #    sql_template - an sql query templated with a value "where_clause"
    #    where_clause_generator - generates a where clause from the multimap data
    #    multi_map data
    #
    def multiplex_query(self, sql_template: str, where_clause: WhereClauseGenerator, multi_map_data: dict):

        results = pd.DataFrame()

        for index in range(10_000_000): #lazy sequence which is much larger than our data
            if index > 1_000_000:
                raise Exception(f"""Seem to have too much data, index is {index}, multimap size is {len(multi_map_data)}, 
                    consider raising range value, or check for infinite loop""")

            found_some = False
            key_val_data: tuple
            key_val_pairs = []
            for key, value in multi_map_data.items():
                if len(value) > index:
                    possible_value: str = value[index]
                    if possible_value is not None:
                        key_val_pairs.append((key, possible_value))
                        found_some = True
            if found_some:
                print(f"Executing query {index+1}, with {len(key_val_pairs)} pairs at {datetime.now()}")
                new_result = self._query(sql_template, where_clause, key_val_pairs)
                print(f"Got result with {len(new_result)} values")
                results = pd.concat([results, new_result])
                index += 1
            if found_some is False:
                break
        return results

    def _query(self, sql_template, where_clause_generator, key_val_pairs):
        sql_where = where_clause_generator.generate(key_val_pairs)
        full_sql = Template(sql_template).substitute({"where": sql_where})

        result = self.biq_query_client.query(full_sql)
        df = pd.DataFrame(key_val_pairs, columns=[where_clause_generator.key_col, where_clause_generator.val_col])
        query_result_df = result.to_dataframe()
        if len(query_result_df) > 0:
            return pd.merge(left=df, right=query_result_df, how="inner", on=where_clause_generator.key_col,
                        validate="one_to_many")
        else:
            return pd.DataFrame()
#%%