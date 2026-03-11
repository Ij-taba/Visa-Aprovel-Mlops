import sys
import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()
# ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                # The constants file provides the URL itself, but we check if an env var exists too
                mongo_db_url = os.getenv("MONGODB_URL", MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"MongoDB URL is not set.")
                MongoDBClient.client = pymongo.MongoClient("mongodb+srv://iijtabahasan:Ijtaba7195@cluster1.tonfxju.mongodb.net/?appName=Cluster1", tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            # logging.info("MongoDB connection succesfull")
        except Exception as e:
            # raise USvisaException(e,sys)
            raise e