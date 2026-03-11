from us_visa.entity.config_entity import ModelPusherConfig
from us_visa.entity.artifact_entity import ModelEvaluationArtifact
from us_visa.entity.s3_estimater import USvisaEstimator
from us_visa.entity.artifact_entity import ModelPusherArtifact
class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig, model_evaluation_artifact: ModelEvaluationArtifact):
        self.model_pusher_config = model_pusher_config
        self.model_evaluation_artifact = model_evaluation_artifact

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        if self.model_evaluation_artifact.is_model_accepted:
            usvisa_estimator = USvisaEstimator(bucket_name=self.model_pusher_config.bucket_name,
                                               model_path=self.model_pusher_config.s3_model_key_path)
            usvisa_estimator.save_model(from_file=self.model_evaluation_artifact.trained_model_path,remove=True)

        model_pusher_artifact = ModelPusherArtifact(
                 is_model_accepted=self.model_evaluation_artifact.is_model_accepted,
                 s3_model_path=self.model_pusher_config.s3_model_key_path,)
        return model_pusher_artifact