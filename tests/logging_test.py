from sivtools.utilities.logging import siv_logger


def test_create_logger():
    logger = siv_logger()

    assert logger


def test_log_with_default_settings(caplog):
    # Arrange
    logger = siv_logger(__name__)

    # Act
    logger.debug('debug test')
    logger.info('info test')

    # Assert
    debug_log = caplog.records[0]
    assert debug_log.levelname == 'DEBUG'
    assert debug_log.message == 'debug test'

    info_log = caplog.records[1]
    assert info_log.levelname == 'INFO'
    assert info_log.message == 'info test'
