# import subprocess

from subprocess_helper import SubprocessHelper
# from logger import CustomLogger, get_logger

def check_sys_ip(logger):
    subprocess_helper = SubprocessHelper(logger)

    cmd = "ip a | grep 'eth0$' | awk \"{print \$2}\""
    ip_a = subprocess_helper.run(cmd)
    ip_a = [ip.split('/')[0] for ip in ip_a.strip().splitlines() if ip.strip()]
    logger.debug(f'В системе {len(ip_a)} ip - {ip_a}.\nВернется первый - {ip_a[0]}')
    return ip_a[0]

    # tmp = ip_a.split('\n')       

    # for i in range(len(tmp)):
    #     logger.debug(f'итерация {i} - {tmp[i]}')
    #     if tmp[i].split(' ')[1] == 'eth0:':
    #         logger.debug(f'найдено зачение, на итерации {i} - {tmp[i].strip().split(" ")[1]}')
    #         for j in range(i, len(tmp)):
    #             logger.debug(f'итерация {i}.{j-i+1} - {tmp[j].split(" ")}')
    #             if tmp[j].split(' ')[3] == 'inet':
    #                 return logger.debug(f'ip сервера - {tmp[j].split(" ")[5]}')
    #         break

    
