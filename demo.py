from us_visa.logger import logging
from us_visa.exception import USvisaException
# logging.info("This is my log mcg")
import sys
try:
    r=3/0
    print('r')
except Exception as e:
    #if i want save this error in log
    # logging.info(e)
    raise USvisaException(e,sys)