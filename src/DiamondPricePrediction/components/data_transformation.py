import pandas as pd
import numpy as np
import os
import sys

from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.DimondPricePrediction.utils.utils import save_object

@dataclass
class Datatransformationconfig:
    preprocessor_obj_file_path= os.path.join("artifacts", 'preprocessor.pkl')

class DataTransformation: 
    def __init__(self):
        self.data_transformation = Datatransformationconfig()

    def get_data_transformation(self):
        try:
            logging.info("initating data transformation ")

             # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )
            
            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]

            )
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor

               
        except Exception as e:
            logging.INFO("Exception at Data Transformation")
            raise customexception(e, sys)
        
    def initalize_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test complete")
            logging.info(f"Train data head: /n{train_df.head().to_string()}")
            logging.info(f"Test data head: /n{test_df.head().to_string()}")

            preprocessing_obj = self.get_data_transformation()

            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']
            
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df= test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Apply preprocessing obj on training and test datasets")
            
            save_object(file_path= self.data_transformation.preprocessor_obj_file_path,
                        obj= preprocessing_obj)
            
            return (
                train_arr,
                test_arr
            )


        except Exception as e:
            logging.info("Exception at Data Transformation")
            raise customexception(e, sys)