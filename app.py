from src.dsmlproject.logger import logging
from src.dsmlproject.exception import CustomException
from src.dsmlproject.components.data_ingestion import DataIngestion
from src.dsmlproject.components.data_ingestion import DataIngestionConfig
# from src.dsmlproject.components.data_transformation import DataTransformationConfig
# from src.dsmlproject.components.data_transformation import DataTransformation
# from src.dsmlproject.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys


if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    #     train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

    #     #data_transformation_config=DataIngestionConfig()
    #     data_transformation=DataTransformation()
    #     train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

    #     #Model Training
    #     model_trainer=ModelTrainer()
    #     print(model_trainer.initiate_model_trainer(train_arr,test_arr))


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    
