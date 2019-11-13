def test_db(driver, url, logging_test):

    logging_test.debug('debug message')
    logging_test.info('info message')
    logging_test.warning('warn message')
    logging_test.error('error message')
    logging_test.critical('critical message')

    pass
