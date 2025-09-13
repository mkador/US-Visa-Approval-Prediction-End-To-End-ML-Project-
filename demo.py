# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# # logging.info("This is my log mcg")
# import sys
# try:
#     r=3/0
#     print('r')
# except Exception as e:
#     #if i want save this error in log
#     # logging.info(e)
#     raise USvisaException(e,sys)

# import os 
# mongodburl = os.getenv("MONGODB_URL")
# print(mongodburl)


from us_visa.pipline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()