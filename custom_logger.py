import logging


class ColoredFormatter(logging.Formatter):
    """
    Кастомный форматтер для цветного вывода и ограничения максимальной длины выводимой строки
    """
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"

    COLORS = {
        'WARNING': YELLOW,
        'INFO': GREEN,
        'DEBUG': BLUE,
        'CRITICAL': YELLOW,
        'ERROR': RED
    }

    MAX_LINE_LENGTH = 600

    DATE_FMT = "%H:%M:%S"

    def __init__(self, msg: str, use_color: bool = True):
        logging.Formatter.__init__(self, msg)
        self._use_color = use_color

    def format(self, record: logging.LogRecord):
        levelname = record.levelname

        if self._use_color and levelname in self.COLORS:
            levelname_colored = self.color_string(levelname, self.COLORS[levelname])
            record.levelname = levelname_colored

        if len(record.msg) > self.MAX_LINE_LENGTH:
            msg = record.msg[:self.MAX_LINE_LENGTH] + "...TRUNCATED"
            if self._use_color:
                msg = record.msg[:self.MAX_LINE_LENGTH] + "..." + self.color_string("TRUNCATED", self.YELLOW)

            record.msg = msg

        return logging.Formatter.format(self, record)

    def formatTime(self, record: logging.LogRecord, datefmt: str):
        return super().formatTime(record, self.DATE_FMT)

    def color_string(self, line: str, color: int):
        return self.COLOR_SEQ % (30 + color) + line + self.RESET_SEQ


class CustomLogger(logging.LoggerAdapter):
    def __init__(self, logger: logging.Logger):
        super().__init__(logger, extra={})
        self._init_stdout_handler()

    def _get_format(self) -> str:
        fmt = "[%(asctime)s] %(levelname)-6s: %(message)s"

        if self.logger.level == logging.DEBUG:
            fmt = "[%(asctime)s] %(levelname)-6s %(filename)s+%(lineno)-4d: %(message)s"

        return fmt

    def _init_stdout_handler(self) -> None:
        formatter = ColoredFormatter(self._get_format())
        handler = logging.StreamHandler()
        handler.setLevel(self.logger.level)
        handler.setFormatter(formatter)

        self._stdout_handler = handler
        self.logger.addHandler(self._stdout_handler)

    def init_file_handler(self, filename: str) -> None:
        formatter = logging.Formatter(self._get_format())
        handler = logging.FileHandler(filename, delay=False)
        handler.setLevel(self.logger.level)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


def get_logger(name: str, log_path: str, debug: bool = False) -> CustomLogger:
    level = logging.INFO

    if debug:
        level = logging.DEBUG

    logger = logging.Logger(name, level)

    custom_logger = CustomLogger(logger)
    custom_logger.init_file_handler(log_path)

    return custom_logger
