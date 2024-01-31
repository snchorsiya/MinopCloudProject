import inspect
import logging


class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".//Logs//logs.log", format="%(asctime)s: %(levelname)s: %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", force=True)
        logerName = inspect.stack()[1][3]
        logger = logging.getLogger(logerName)
        logger.setLevel(logging.INFO)
        return logger