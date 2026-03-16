# Logging in Python is used to record events that happen while a program run
# Debugging programs
# Tracking errors in production
# Monitoring application behavior
# Saving logs to files for later analysis
"""
import logging
#logging.warning("this is a warning message")
#logging.error("this is a error message")
#logging.critical("this is a critical message")

#print()
#DEBUG	- Detailed debugging information
#INFO	- General information
#WARNING	- Something unexpected happened
#ERROR	- A serious problem occurred
#CRITICAL - Program may stop running

#logging.debug("this is a debug message")
#logging.info("this is a info message")
#logging.warning("this is a warning message")
#logging.error("this is a error message")
#logging.critical("this is a critical message")

#seting logging level
"""
#logging.basicConfig(level=logging.INFO)
#logging.debug("this is a debug configuration")
#logging.info("this is a life message")
#logging.warning("this is a warning message")
#logging.error("this is a error message")
"""
logging.basicConfig(
    level=logging.INFO,
    filename="app.log"
)
logging.info("Program started")
logging.warning("Low memory warning")
logging.error("An error occurred")
"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.error("Something failed")
