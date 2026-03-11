from us_visa.configuration import Mongodb_connection
import pandas as pd
from us_visa.constants import DATABASE_NAME
import numpy as np
class USvisaData:
   def __init__(self):
      self.mongo_client = Mongodb_connection.MongoDBClient(database_name=DATABASE_NAME)
   def export_collection_as_dataframe(self, collection_name):
        database=self.mongo_client.database
        collection=database[collection_name]
        df=pd.DataFrame(list(collection.find()))
        if "_id" in df.columns:
            df=df.drop("_id", axis=1)
        df.replace({"na": np.nan}, inplace=True)
        return df
    