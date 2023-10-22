import unittest

import pandas as pd

from detectdd.auth_bigquery import BigQueryClient
from detectdd.query_multiplexer import QueryMultiplexer, WhereClauseGenerator


class QueryMultiplexerTestCase(unittest.TestCase):

    def test_multiplexer(self):
        mock = BigQueryClientMock()
        query_multiplexer = QueryMultiplexer(mock)
        query_multiplexer.multiplex_query("SELECT * FROM input_events WHERE ($where)",
                                          WhereClauseGenerator("(stay_id = '$stay_id' AND starttime = '$starttime')", "stay_id", "starttime"),
                                          {"1": list([1, 2, 3, 4]), "2": list([4, 5, 6])})

        self.assertEqual(4, len(mock.queries))
        self.assertEqual(
            "SELECT * FROM input_events "
            "WHERE ((stay_id = '1' AND starttime = '1') OR (stay_id = '2' AND starttime = '4'))",
            mock.queries[0])

        self.assertEqual(
            "SELECT * FROM input_events "
            "WHERE ((stay_id = '1' AND starttime = '2') OR (stay_id = '2' AND starttime = '5'))",
            mock.queries[1])

        self.assertEqual(
            "SELECT * FROM input_events "
            "WHERE ((stay_id = '1' AND starttime = '3') OR (stay_id = '2' AND starttime = '6'))",
            mock.queries[2])

        self.assertEqual(
            "SELECT * FROM input_events "
            "WHERE ((stay_id = '1' AND starttime = '4'))",
            mock.queries[3])
class BigQueryClientMock:

    def __init__(self):
        self.queries = []

    # mock the query method, capture the sql
    def query(self, sql):
        self.queries.append(sql)
        return QueryResultMock()


class QueryResultMock:
    def to_dataframe(self):
        return pd.DataFrame()


if __name__ == '__main__':
    unittest.main()

# %%
