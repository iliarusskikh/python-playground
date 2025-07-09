import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
#logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    1/0
except ZeroDivisionError as e:
    #logging.error("ZeroDivisionError", exc_info=True)
    logging.exception("ZeroDivisionError")


logger = logging.getLogger("mylogger")#__name__ name of a current module

handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Test the custom logger")
