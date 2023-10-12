from google.cloud import bigquery
import google.auth
#%%
class BigQueryClient:
    @staticmethod
    def _get_client(c,p):
        return bigquery.Client(p, c)

    @staticmethod
    def _get_gcreds(scopes = None):
        if scopes is None:
            scopes = ["https://www.googleapis.com/auth/bigquery"]
        return google.auth.default(
            scopes )

    @staticmethod
    def auth():
        cred = BigQueryClient._get_gcreds()
        print(*cred)
        return BigQueryClient._get_client(*cred)