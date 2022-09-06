import logging

logging.basicConfig(filename='mylog.log', level=logging.CRITICAL)
logging.critical( 'Critical')
logging.error('Error')
logging.warning('Warning')
logging.info('Info')
logging.debug('Debug')
