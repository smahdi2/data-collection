import redshift_connector
import pandas as pd

class DataCollection:
    def __init__(self, host, database, port, user, password):
        self.connection = redshift_connector.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def read_data(self, query):
        self.cursor.execute(query)
        result: tuple = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        return pd.DataFrame(result, columns=column_names)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()