import logging
'''
5 log message levels:
Debug
Info
Warning
Error
Critical
'''
LOGFORMAT="%(levelname)s - %(user)s   %(asctime)s - %(message)s"
logging.basicConfig(filename="output.log",level=logging.DEBUG,format=LOGFORMAT,filemode='w')
logger=logging.getLogger()
logger.debug("Job details")
logger.info("Job details")
logger.warning("Job details")
logger.error("Job details")
logger.critical("Job details")
