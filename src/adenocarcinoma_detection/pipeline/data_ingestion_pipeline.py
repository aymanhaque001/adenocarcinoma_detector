

from adenocarcinoma_detection.config.configuration import ConfigurationManager
from adenocarcinoma_detection.components.data_ingestion import DataIngestion
from adenocarcinoma_detection import logger



STAGE = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



def DataIngestionStart():
    
    try:
        logger.info(f"Data Ingestion Pipeline Started")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"Data Ingestion Completed")
    
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    
    DataIngestionStart() 