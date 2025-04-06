import logger
import argparse

parser = argparse.ArgumentParser(
    prog="vps-moove-hestia",
    description="Auto vps move",
    epilog="Example of calling a script: <pattern>",
    add_help=False,
)


parser.add_argument("-u", "--user", help="Логин хоста", required=True)

parser.add_argument("-h", "--host", help="host откуда синкаем", required=True)
parser.add_argument(
    "-w",
    "--web-root",
    help="Путь расположения файлов на исходном сервере",
    required=True,
)
parser.add_argument(
    "-p",
    metavar="PORT",
    help="Задать порт ssh в случае если на исходном сервере кастомный порт",
)
parser.add_argument(
    "--pas",
    metavar="PASSWORD",
    help="Если нельзя прокинуть ключ, то можно для автоматизаци задать пароль",
)
parser.add_argument("--fix-permission", help="Исправление прав")
parser.add_argument(
    "--php", help="Задать требуемую версию php при разворачивании автоматически"
)
parser.add_argument(
    "--log-file",
    help="Кастомный путь до лог файла, удобнее когда много сайтов переносится",
)
parser.add_argument("--help", action="help")


args = parser.parse_args()

log = logger.setup_logger()

log.info("test start")


def main():
    log.warning("test main")
    pass


if __name__ == "__main__":
    main()
