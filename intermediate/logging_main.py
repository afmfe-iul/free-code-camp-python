from datetime import date
import logging
import traceback

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

import logging_helper

try:
    a = [1, 2, 3]
    val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)
except:
    logging.error("The error is %s", traceback.format_exc())
