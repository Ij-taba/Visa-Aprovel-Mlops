from us_visa.componenets.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.config_entity import DataValidationConfig

from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.componenets.data_validation import DataValidation
from us_visa.entity.artifact_entity import DataValidationArtifact
from us_visa.componenets.data_transformation import DataTransformation
from us_visa.entity.config_entity import DataTransformationConfig
from us_visa.componenets.model_training import ModelTrainer
from us_visa.entity.config_entity import ModelTrainerConfig
from us_visa.componenets.model_evaluation import ModelEvaluation
from us_visa.entity.config_entity import ModelEvaluationConfig
from us_visa.entity.artifact_entity import ModelTrainerArtifact
from us_visa.entity.artifact_entity import ModelEvaluationArtifact
from us_visa.componenets.model_pusher import ModelPusher
from us_visa.entity.config_entity import ModelPusherConfig
# model_eval_config: ModelEvaluationConfig, data_ingestion_artifact: DataIngestionArtifact,
#                  model_trainer_artifact: ModelTrainerArtifact
class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_ingestion_artifact = None
        self.data_validation_artifact = None
    def start_data_ingestion(self,DataIngestionConfig) -> DataIngestionArtifact:
        data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
        self.data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        return self.data_ingestion_artifact    
    def start_data_validation(self):
        data_validation_config = DataValidationConfig()
        data_validation=DataValidation(data_ingestion_artifact=self.data_ingestion_artifact,data_validation_config=data_validation_config)
        self.data_validation_artifact = data_validation.initiate_data_validation()
        return self.data_validation_artifact
    def start_data_transformation(self):
        data_transformation_config = DataTransformationConfig()
        data_transformation=DataTransformation(data_ingestion_artifact=self.data_ingestion_artifact,data_transformation_config=data_transformation_config,data_validation_artifact=self.data_validation_artifact)
        d=data_transformation.initiate_data_transformation()
        return d
    def start_model_trainer(self):
        model_trainer_config = ModelTrainerConfig()
        model_trainer=ModelTrainer(data_transformation_artifact=self.start_data_transformation(),model_trainer_config=model_trainer_config)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        return model_trainer_artifact    
    def start_model_evaluation(self):
        model_eval_config = ModelEvaluationConfig()
        model_evaluation=ModelEvaluation(model_eval_config=model_eval_config,data_ingestion_artifact=self.data_ingestion_artifact,model_trainer_artifact=self.start_model_trainer())
        model_evaluation_artifact=model_evaluation.initiate_model_evaluation()
        return model_evaluation_artifact
    def start_model_pusher(self):
        model_pusher_config = ModelPusherConfig()
        model_pusher=ModelPusher(model_pusher_config=model_pusher_config,model_evaluation_artifact=self.start_model_evaluation())
        model_pusher_artifact=model_pusher.initiate_model_pusher()
        return model_pusher_artifact
    