import os
import dill
import sys

from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
from dataclasses import dataclass


def save_object(filename,obj):
    try:
        dir_path=os.path.dirname(filename)
        os.makedirs(dir_path,exist_ok=True)
        with open(filename,'wb') as f:
            dill.dump(obj,f)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(models,X_train,y_train,X_test,y_test):
    try:
        report={}
        
        for i in range(len(list(models))):
            model=list(models.values())[i]
            # para=params[list(models.keys())[i]]

            # gs=GridSearchCV(model,para,cv=3)
            # gs.fit(X_train,y_train)
# 
            # model.set_params(**gs.best_params_)
            # model.fit(X_train,y_train)

            model.fit(X_train,y_train)
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score
        return report
    except Exception as e:
        raise CustomException(e,sys)