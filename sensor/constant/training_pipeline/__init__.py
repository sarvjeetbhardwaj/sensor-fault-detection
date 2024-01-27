import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

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
