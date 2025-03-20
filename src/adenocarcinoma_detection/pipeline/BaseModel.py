

from adenocarcinoma_detection.config.configuration import ConfigurationManager
from adenocarcinoma_detection.components.BaseModel import PrepareBaseModel
from adenocarcinoma_detection import logger

STAGE= "Base_Model"


class BaseModelPipeline:
    
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_prepare_base_model_config()
        base_model = PrepareBaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


def StartBaseModel():
    
    try:
        
        logger.info(f"Starting to Prepare {STAGE}")
        obj = BaseModelPipeline()
        obj.main()
        logger.info(f"{STAGE} completed")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    
    StartBaseModel()  