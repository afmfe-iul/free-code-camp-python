import logging
import logging.config

# Define loggers without config file
logger = logging.getLogger(__name__)

# create handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this is a error")


# Define loggers with config file
logging.config.fileConfig("logging.conf")

logger_from_config_file = logging.getLogger("simpleExample")
logger_from_config_file.debug("this is a debug message")

# There's also possible to define loggers with a dictionary via logging.config.dictConfig()
