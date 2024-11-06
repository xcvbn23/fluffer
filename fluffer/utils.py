import logging


def setup_logger(mod, log_level=logging.DEBUG) -> logging.Logger:
    stream_handler = logging.StreamHandler()

    logger = logging.getLogger(mod)
    logger.addHandler(stream_handler)
    logger.setLevel(log_level)

    return logger
