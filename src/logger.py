import logging 
import os
from datetime import datetime

LOG_FILE= f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)


os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    file_name = LOG_FILE_PATH,
    format = "[%(asctime)s] %(levelname)s: %(message)s",
    level = logging.INFO,
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)