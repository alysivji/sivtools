import logging


DEFAULT_FORMAT_STRING = (
    '[%(levelname)s] %(name)s:%(lineno)s (%(asctime)s) %(message)s')


def siv_logger(name='app', *, format_str=DEFAULT_FORMAT_STRING,
               level=logging.DEBUG, handler=logging.StreamHandler):
    """
    Wrapper for Standard Library logger with sane defaults
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(format_str)

    ch = handler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
