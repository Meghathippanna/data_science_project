from src.DimondPricePrediction.components.data_ingestion import Data_Ingestion

from src.DimondPricePrediction.components.data_transformation import DataTransformation

from src.DimondPricePrediction.components.model_trainer import ModelTrainer


import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd


data_ingest=Data_Ingestion()

train_data_path,test_data_path= data_ingest.data_ingestion_initalize()
data_transformation = DataTransformation()
train_arr,test_arr=data_transformation.initalize_data_transformation(train_data_path,test_data_path)

model_trainer=ModelTrainer()
model_trainer.initate_model_training(train_arr,test_arr)