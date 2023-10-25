# __init_.py is used so that components folder can be used as a package
#  components contains all the various modules/parts/chapters for traininf purposes we will be doing in our project

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
        train_data_path: str = os.path.join('artifacts','train.csv')
        test_data_path: str = os.path.join('artifacts','test.csv')
        raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method/component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")                       #Reading the dataset
            logging.info("read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)            #saving the df(raw) to designated folder using ingestion_config

            logging.info("Train test split initiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)            #same as 31 except diff folder
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)              #done the splitting saving now in artifact folder

            logging.info("Ingestion of data completed")            

            return(
                 self.ingestion_config.train_data_path,
                 self.ingestion_config.test_data_path
            )
        except Exception as e: 
            raise CustomException(e,sys)

if __name__ == "__main__":
     obj = DataIngestion()
     obj.initiate_data_ingestion()