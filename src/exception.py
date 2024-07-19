import sys 
import logging
def error_msg_details(error, error_details:sys):
    _, _, exc_tb = error_details.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    lineNumber = exc_tb.tb_lineno
    return f"Error occured in script: [{fileName}] at line number: [{lineNumber}] error message: [{error}]" 

class CustomeException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_msg_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero Exception")
        raise CustomeException(e, sys)

    