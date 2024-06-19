import pandas as pd
import numpy as np
import sys
import os
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
from sklearn.model_selection import train_test_split
from pathlib import Path
from dataclasses import dataclass 

class Data_ingestion_config:
    raw_data_path:str= os.path.join("artifacts","raw_data.csv")
    train_data_path:str = os.path.join("artifacts", "train_data.csv")
    test_data_path:str = os.path.join("artifacts", "test_data.csv")

class Data_Ingestion:
    def __init__(self):
        self.ingestion_config =Data_ingestion_config()

    def data_ingestion_initalize(self):
        logging.info("Data Ingestion Started")

        try:
            data= pd.read_csv(Path(os.path.join("notebooks/data/", "gempredcition.csv")))
            logging.info("Dataset read as dataframe and labelled")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok = True)
            data.to_csv(self.ingestion_config.raw_data_path, index= False)
            logging.info("Raw data file added to artifacts")

            logging.info("Initalizing Train and Test Splitting") 

            Train_data, Test_data= train_test_split(data, test_size=0.25)
            logging.info("Train and Test split completed")

            Train_data.to_csv(self.ingestion_config.train_data_path, index = False)
            Test_data.to_csv(self.ingestion_config.test_data_path, index= False)

            logging.info("Train and Test split data added to artifacts")
            logging.info("Data Ingestion part completed")

            return (
                 
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            

            
        
        except Exception as e:
            logging.info("Exception occured during Data Ingestion")
            raise customexception(e, sys)