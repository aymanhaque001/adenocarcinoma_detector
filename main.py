from adenocarcinoma_detection import logger
from adenocarcinoma_detection.pipeline.BaseModel import StartBaseModel
from src.adenocarcinoma_detection.pipeline.data_ingestion_pipeline import DataIngestionPipeline, DataIngestionStart
from adenocarcinoma_detection.pipeline.model_training import model_training_start
from adenocarcinoma_detection.pipeline.Model_evaluation import Evaluation_Stage
 
"""PIPELINE"""
DataIngestionStart() 
StartBaseModel() 
model_training_start()
Evaluation_Stage()


