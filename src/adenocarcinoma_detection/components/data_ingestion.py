import os
import zipfile
import gdown
from adenocarcinoma_detection.entity.config_entity import DataIngestionConfig
from adenocarcinoma_detection.utils.common import get_size
from adenocarcinoma_detection import logger




class DataIngestion:
    
    def __init__(self, config: DataIngestionConfig):
        
        self.config = config


    def download_file(self):
        
        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded file from {dataset_url} into the directory: {zip_download_dir}")

        except Exception as e:
            raise e
        
        
        
        
    def extract_zip_file(self):
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)