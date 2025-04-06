from adenocarcinoma_detection.config.configuration import ConfigurationManager
from adenocarcinoma_detection.components.mlflow_evaluation import Evaluation
from adenocarcinoma_detection import logger



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

def Evaluation_Stage():
    
    try:
        
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"Evaluation Completed. Check mlflow ui. ")
    except Exception as e:
        logger.exception(e)
        raise e
    


if __name__ == '__main__':
    
    Evaluation_Stage()
            