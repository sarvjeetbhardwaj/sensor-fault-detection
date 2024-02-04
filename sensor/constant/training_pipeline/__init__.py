import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

SAVED_MODEL_DIR = 'saved_models'

# defining common constant variable for training pipeline
TARGET_COLUMN = 'class'
PIPELINE_NAME = 'sensor'
ARTIFACT_DIR = 'artifact'
FILE_NAME = 'sensor.csv'

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
MODEL_FILE_NAME = 'model.pkl'
SCHEMA_FILE_PATH = os.path.join('config', 'schema.yaml')
SCHEMA_DROP_COLS = 'drop_columns'

# DataIngestion related constant strat with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTION_NAME = 'sensor-data'
DATA_INGESTION_DIR_NAME = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'
DATA_INGESTION_INGESTED_DIR = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION = 0.2

# DataValidation related constants

DATA_VALIDATION_DIR_NAME = 'data_validation'
DATA_VALIDATION_VALID_DIR = 'validated'
DATA_VALIDATION_INVALID_DIR = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = 'report.yaml'


# Data Tranformation related constants
DATA_TRANSFORMATION_DIR_NAME = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = 'transformed_object'

# Model Trainer related constant
MODEL_TRAINER_DIR_NAME = 'model_trainer'
MODEL_TRAINER_TRAINER_MODEL_DIR = 'trained_model'
MODEL_TRAINER_TRAINED_MODEL_NAME = 'model.pkl'
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD= 0.6

## Model evaluation related constants
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_EVALUATION_DIR_NAME = 'model_evaluation'
MODEL_EVALUATION_REPORT_NAME = 'report.yaml'

## Model pusher related constants
MODEL_PUSHER_DIR_NAME = 'model_pusher'
MODEL_PUSHER_SAVED_MODEL_DIR = SAVED_MODEL_DIR


