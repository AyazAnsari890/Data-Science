import os #because we have to create file that contain training, test data in some specific path inside the artifact folder.
import sys #for logging excepiton
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
'''
In Python, a data class is a class that is designed to only hold data values. 
They aren't different from regular classes, but they usually don't have any other methods. 
They are typically used to store information that will be passed between different parts of a program or a system.
'''

## Initialize the Data Ingestion Configuration

@dataclass #for directly creating class variables w/o creating __init__ methd
class DataIngestionconfig:
    #Create variables where we will store the path of our train and test data
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

## Create the data ingestion class

class DataIngestion:
    def __init__(self):
        #Here we initialized the previously created variables
        self.ingestion_config=DataIngestionconfig()

    #In this method we are reading the csv file, saving the raw data path, doing train test split
    #and finally saving the train test data at the location specified and finally returning the data
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")

        try:
            df = pd.read_csv(os.path.join('notebooks/data', 'gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')
            ##pass

            #make directory (artifacts directory is already made, just for sake)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False) #save our file into this specific path

            logging.info('Raw data is created')

            #Define train, test data
            train_set, test_set=train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e, sys)
    