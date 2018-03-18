import logging


def siv_logger(name='app', *, formatter=None, level=logging.DEBUG,
               handler=logging.StreamHandler, handler_level=logging.DEBUG):
    """
    Wrapper for Standard Library logger with sane defaults
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if formatter is None:
        formatter = logging.Formatter(
            '[%(levelname)s] %(name)s:%(lineno)s (%(asctime)s) %(message)s')

    ch = handler()
    ch.setLevel(handler_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
