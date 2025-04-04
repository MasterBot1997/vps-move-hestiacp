import logging

def setup_logger():
    logger = logging.getLogger("hestia_migrator")
    logger.setLevel(logging.DEBUG)

    # Консольный вывод
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger


