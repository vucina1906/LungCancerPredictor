import sys
import logging

#We create function that cath error and error details
def format_error(error,error_details):
    _,_, exc_tb = error_details.exc_info() # We catch only third place holder from error detail and catch it as exc_tb (exceptipon traceback)
    file_name = exc_tb.tb_frame.f_code.co_filename #From exception traceback we get the name of the file in which error occurred
    line_number = exc_tb.tb_lineno #From exception traceback we get the number of line in which error occurred
    error_message = f"Error occurred in {file_name}, line {line_number}: {error}" #We form the message
    return error_message

class CustomException(Exception):#We create a class that inherit everything from built-in exception class
    def __init__(self,error,error_detail):#This is constructor method for class that takes two parameters.Error (the error message) and error_detail (that comes from exc_info())
        self.error_message = format_error(error,error_detail)#now we call function we created up and take error and error details and create formated string
        super().__init__(self.error_message)#This calls __init__ method of parent built in Exception class wit error message argument. It is necessery to inherit from built in Exception class so our class can later catch error and raise them.
    
    def __str__(self):
        return self.error_message


