import sys
import os
sys.path.append("d:/Visa Aprovel Mlops")

from us_visa.pipeline.training import TrainPipeline

try:
    pipeline = TrainPipeline()
    artifact = pipeline.start_data_ingestion(None) # passing None because it is unused
    artific=pipeline.start_data_validation()
    s=pipeline.start_data_transformation()
    # ss=pipeline.start_model_trainer()
    ss=pipeline.start_model_evaluation()
    sss=pipeline.start_model_pusher()
    print(f"Artifact created: {artifact}")
except Exception as e:
    import traceback
    traceback.print_exc()
