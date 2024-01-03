import os
import dill
import sys
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