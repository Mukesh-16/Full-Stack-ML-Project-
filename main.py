from src.ML_Project import logger
from ML_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ML_Project.pipeline.stage_02_data_validation import DataValidationPipeline
from ML_Project.pipeline.stage_03_data_transformation import DataTransformationPipeline
from ML_Project.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from ML_Project.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "DATA INGESTION"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA VALIDATION"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "DATA TRANSFORMATION"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model Training"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model Evaluation"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e