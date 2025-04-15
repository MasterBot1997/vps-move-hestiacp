import string
import random

from logger import CustomLogger
from subprocess_helper import SubprocessHelper

class HestiaCPHelper():
    
    def __init__(self, logger: CustomLogger):
        self._logger = logger
        self._subprocess_helper = SubprocessHelper(self._logger)

    def _create_pas(self, length:int=12) -> str:
        # Используем только цифры и буквы (заглавные и строчные)
        characters = string.ascii_letters + string.digits
        # Генерируем случайный пароль
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def _list_php(self):

        cmd = 'v-list-web-templates-backend | grep PHP'

        stdout = self._subprocess_helper.run(cmd)
        return stdout
    
    pass