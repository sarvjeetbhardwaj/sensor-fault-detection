import os
from datetime import datetime
from sensor.constant.training_pipeline import PIPELINE_NAME, ARTIFACT_DIR,DATA_INGESTION_DIR_NAME,\
                                             DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME,\
                                             DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME,\
                                             DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME,\
                                             DATA_INGESTION_TRAIN_TEST_SPLIT_RATION,\
                                             DATA_INGESTION_COLLECTION_NAME
from sensor.constant import training_pipeline





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


class DataValidationConfig:

    def __init__(self, training_pipeine_config:TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeine_config.artifact_dir,
                                                training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir = os.path.join(self.data_validation_dir,
                                           training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir = os.path.join(self.data_validation_dir,
                                             training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path = os.path.join(self.valid_data_dir,
                                             training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path = os.path.join(self.valid_data_dir,
                                             training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path = os.path.join(self.invalid_data_dir,
                                             training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path = os.path.join(self.invalid_data_dir,
                                             training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path = os.path.join(self.data_validation_dir, 
                                                   training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
                                                   training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
        

class DataTransformationConfig:
    def __init__(self, training_pipeine_config:TrainingPipelineConfig):
        self.data_transformation_dir = os.path.join(training_pipeine_config.artifact_dir,
                                                    training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path = os.path.join(self.data_transformation_dir, 
                                                        training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                        training_pipeline.TRAIN_FILE_NAME.replace('csv', 'npy'))
        self.transformed_test_file_path = os.path.join(self.data_transformation_dir, 
                                                        training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                        training_pipeline.TEST_FILE_NAME.replace('csv', 'npy'))
        self.transformed_object_file_path = os.path.join(self.data_transformation_dir, 
                                                        training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                        training_pipeline.PREPROCESSING_OBJECT_FILE_NAME.replace('csv', 'npy'))