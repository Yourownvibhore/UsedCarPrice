import os
import dill
import sys
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import save_object
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

@dataclass
class ModelTrainerConfig:
    model_pkl_file_path=os.path.join('artifact','model.pkl')

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer=ModelTrainerConfig()
    
    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("Initiating model training")
            logging.info("splitting the data into X_train,y_train,X_test,y_test")
            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1],
            )
        except Exception as e:
            raise CustomException(e,sys)