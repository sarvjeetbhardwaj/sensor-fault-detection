import os
from datetime import datetime
from sensor.constant.training_pipeline import PIPELINE_NAME, ARTIFACT_DIR,DATA_INGESTION_DIR_NAME,\
                                             DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME,\
                                             DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME,\
                                             DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME,\
                                             DATA_INGESTION_TRAIN_TEST_SPLIT_RATION,\
                                             DATA_INGESTION_COLLECTION_NAME





class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime("%Y-%m-%d_%H_%M_%S")
        self.pipeline_name = PIPELINE_NAME
        self.artifact_dir =  os.path.join(ARTIFACT_DIR, timestamp)
        self.timestamp = timestamp

class DataIngestionConfig:

    def __init__(self, training_pipeine_config:TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(training_pipeine_config.artifact_dir, 
                                               DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir, 
                                                   DATA_INGESTION_FEATURE_STORE_DIR,
                                                   FILE_NAME)
        self.training_file_path = os.path.join(self.data_ingestion_dir,
                                               DATA_INGESTION_INGESTED_DIR,
                                               TRAIN_FILE_NAME)
        self.testing_file_path = os.path.join(self.data_ingestion_dir,
                                              DATA_INGESTION_INGESTED_DIR,
                                              TEST_FILE_NAME)
        self.train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name = DATA_INGESTION_COLLECTION_NAME 


