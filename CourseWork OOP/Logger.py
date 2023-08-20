import logging
from datetime import datetime


class Logger:

    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        encoding='utf-8',
                        format='%(asctime)s %(levelname)s %(message)s')
    # logging.debug("A DEBUG Message")
    # logging.info("An INFO")
    # logging.warning("A WARNING")
    # logging.error("An ERROR")
    # logging.critical("A message of CRITICAL severity")

    def get_logging(text):
        logging.info(text)
        print(f'{str(datetime.now())[:-3]} {text}')
