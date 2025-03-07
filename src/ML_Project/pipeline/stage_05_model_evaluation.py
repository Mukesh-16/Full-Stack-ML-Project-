from ML_Project.config.configuration import ConfigurationManager
from ML_Project.components.model_evaluation import ModelEvaluation
from ML_Project import logger
import os

STAGE_NAME = "Model Evaluation"

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/mbairu/Full-Stack-ML-Project-.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="mbairu"
os.environ["MLFLOW_TRACKING_PASSWORD"]="87385c32a7a01dc959f1d28f0bfa41836563e153"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e