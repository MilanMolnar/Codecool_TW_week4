import logging

#Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "job_hunter.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    datefmt='%d-%b-%y %H:%M:%S',
                    filemode="w")
logger = logging.getLogger()

#using: logger.info("text") / logger.debug("text") / logger.warning("text")