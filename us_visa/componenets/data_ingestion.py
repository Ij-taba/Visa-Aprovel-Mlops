from us_visa.entity.config_entity import DataIngestionConfig 
from us_visa.data_access import usvisa_data
from us_visa.constants import *
from us_visa.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from pandas import DataFrame
from us_visa.data_access.usvisa_data import USvisaData
class DataIngestion:
     def __init__(self, data_ingestion_config:DataIngestionConfig):
         self.data_ingestion_config=data_ingestion_config
     
     def export_data_into_feature_store(self)->DataFrame:
          usVisa=USvisaData()
          dataframe=usVisa.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
          feature_store_file_path=self.data_ingestion_config.feature_store_file_path
          dir_path=os.path.dirname(feature_store_file_path)
          os.makedirs(dir_path, exist_ok=True)
          dataframe.to_csv(feature_store_file_path,index=False)
          return dataframe
     def  train_test_split(self,data):
          train_file_path=self.data_ingestion_config.train_file_path
          test_file_path=self.data_ingestion_config.test_file_path
          dir_path=os.path.dirname(train_file_path)
          test_path=os.path.dirname(test_file_path)
          train_set,test_set=train_test_split(data,test_size=self.data_ingestion_config.train_test_split,random_state=42)
          os.makedirs(dir_path,exist_ok=True)
          train_set.to_csv(train_file_path,index=False,header=True)
          print(train_set)
          os.makedirs(test_path,exist_ok=True)
          test_set.to_csv(test_file_path,index=False,header=True)
     def initiate_data_ingestion(self) ->DataIngestionArtifact:
          dataframe=self.export_data_into_feature_store()
          self.train_test_split(dataframe)

          return DataIngestionArtifact(trained_file_path=self.data_ingestion_config.train_file_path,
                         test_file_path=self.data_ingestion_config.test_file_path)    

if __name__ == "__main__":
    from us_visa.pipeline.training import TrainPipeline
    print("Starting data ingestion process...")
    try:
        pipeline = TrainPipeline()
        artifact = pipeline.start_data_ingestion(None)
        print(f"Data ingestion successful! Artifacts created at:\nTrain: {artifact.train_file_path}\nTest: {artifact.test_file_path}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\nError occurred: {e}")