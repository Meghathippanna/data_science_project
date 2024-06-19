import logging
import os
from datetime import datetime

datetime.now()

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path= os.path.join(os.getcwd(), 'logs')
os.makedirs(log_path, exist_ok=True)
log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO, filename=log_file_path, format="[%(asctime)s] %(lineno)d %(name)s - %(message)s")