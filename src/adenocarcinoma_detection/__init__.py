import os
import sys
import logging


log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)
log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(
    level= logging.INFO,
    format= log_format,
    
    handlers=[
        
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        
    ]
)


logger = logging.getLogger("Logger")