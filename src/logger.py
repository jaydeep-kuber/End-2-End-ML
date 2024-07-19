# logger is to log changes in text file like errors, exceptions anf all.

# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%D_%M_%Y_%H_%M_%S')}.log"
# LOGS_PATH = os.path.join(os.getcwd(),"logs", LOG_FILE)

# os.makedirs(LOGS_PATH, exist_ok = True) # make dir even if i have 

# LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

if __name__ == "__main__":
    logging.info("Logging has started")