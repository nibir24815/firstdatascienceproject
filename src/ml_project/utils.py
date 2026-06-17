import os
import sys
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv
import pickle
import numpy as np

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("Reading data from SQL database started.")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,db=db)
        logging.info("connection established",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    