import argparse
import os

from custom_logger import get_logger

def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog='vps-moove-hestia',
        epilog='Example of calling a script: <pattern>',
        # add_help=False
        conflict_handler='resolve'
    )


    parser.add_argument(
        '-u', 
        '--user', 
        help='ssh user',
        default='user', 
        required=True
    )

    parser.add_argument(
        '-h', 
        '--host', 
        help='ssh host', 
        required=True
    )

    parser.add_argument(
        '-w',
        '--web-root',
        help='full path of web root on ssh host, for example: /home/t/testuser/testdomain.ru/public_html',
        required=True,
    )

    parser.add_argument(
        '-p',
        '--port',
        metavar='PORT',
        type=int,
        default=22,
        help='ssh port',
    )

    parser.add_argument(
        '--pas',
        metavar='PASSWORD',
        help='ssh password',
    )

    parser.add_argument(
        '--php', 
        help='Задать требуемую версию php при разворачивании автоматически'
    )

    parser.add_argument(
        '--fix-permission',
        action='store_true', 
        help='Исправление прав'
    )

    parser.add_argument(
        '--delete-old-files',
        action='store_true',
        help='delete old files in ispmanager web root before deploying'
    )


    parser.add_argument(
        '--log-file',
        help='Custom log file, for example: test_site.log',
    )

    parser.add_argument(
        '--help', 
        action='help'
    )

    parser.add_argument(
        '--debug', 
        action='store_true',
        help='display debug info', 
    )

    return parser.parse_args()


# log = get_logger.setup_logger()

# log.info('test start')


def main():
    args = parse_args()
    # log.info('Start move')
    print(args)
    pass


if __name__ == '__main__':
    main()
    # os.path.realpath(log_path)
    # print(os.path.dirname(os.path.realpath(__file__)))
    current_dir = os.path.dirname(os.path.realpath(__file__))

    log_path = os.path.join(current_dir, '../deploy_log', 'deploy.log')
    log_path = os.path.realpath(log_path)
    print(log_path)
