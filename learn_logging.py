import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)
logger = logging.getLogger()

logger.info('test info')
logger.warning('test warning')
logger.debug('this is debug')
logger.critical('this is critical')