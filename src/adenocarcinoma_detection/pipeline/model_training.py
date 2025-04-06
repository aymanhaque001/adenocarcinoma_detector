from adenocarcinoma_detection.config.configuration import ConfigurationManager
from adenocarcinoma_detection.components.ModelTraining import Training
from adenocarcinoma_detection import logger



STAGE = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

def model_training_start():
    try:
        logger.info(f"Model Training Started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Model training Completed")
    except Exception as e:
        logger.exception(e)
        raise e
        

if __name__ == '__main__':
    model_training_start()