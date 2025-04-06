import logging

# ANSI-цвета
LOG_COLORS = {
    "DEBUG": "\033[94m",  # синий
    "INFO": "\033[92m",  # зелёный
    "WARNING": "\033[93m",  # жёлтый
    "ERROR": "\033[91m",  # красный
    "CRITICAL": "\033[95m",  # фиолетовый
    "RESET": "\033[0m",  # сброс
}


class ColorFormatter(logging.Formatter):
    def format(self, record):
        color = LOG_COLORS.get(record.levelname, LOG_COLORS["RESET"])
        reset = LOG_COLORS["RESET"]
        record.levelname = f"{color}{record.levelname}{reset}"
        return super().format(record)


def setup_logger():
    logger = logging.getLogger("hestia_migrator")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = ColorFormatter("[%(asctime)s] %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)

    return logger


# log.debug("Отладочная инфа")
# log.info("Инфо сообщение")
# log.warning("Внимание")
# log.error("Ошибка")
# log.critical("Критическая ошибка")
