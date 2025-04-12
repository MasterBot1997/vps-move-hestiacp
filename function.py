import subprocess
import string
import random

# Создаем пароль
def create_pas(length:int=12) -> str:
    # Используем только цифры и буквы (заглавные и строчные)
    characters = string.ascii_letters + string.digits
    # Генерируем случайный пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def create_user(name_user:str='user'):
    # check_user(name_user) # После создания чеков активировать
    # Команда для создания пользователя, после проверки если его нет
    command = f'v-add-user {name_user} "{create_pas(12)}" example@exampl.com'
    # Выполнение команды, что пользователь создан
    subprocess.run(['bash', '-c', command], capture_output=True, text=True)
# Попробовать обыграть через try exept

def creat_web_domain(domain, user='user'):
    command = f'v-add-web-domain {user} {domain}'
    subprocess.run(['bash', '-c', command], capture_output=True, text=True)


def create_database(domain, user='user'):
    # Имя БД и пользователя БД создается на основе домена
    # Так как в HestiaCP есть ограничение на имя БД мы его умышленно обрезаем на случай длинных домено
    db_name = domain.replace(".","_")[:12]
    # Команда для добавления БД
    command = f'v-add-database {user} {db_name} {db_name} "{create_pas(12)}"'
    # Выполнение команды
    subprocess.run(['bash', '-c', command], capture_output=True, text=True)



def fix_permission(domain, user='user'):
    subprocess.run(['bash', '-c', f"find /home/{user}/web/{domain}/public_html -type d -exec chmod 755"+" '{}' \;"], capture_output=True, text=True)
    subprocess.run(['bash', '-c', f"find /home/{user}/web/{domain}/public_html -type f -exec chmod 644"+" '{}' \;"], capture_output=True, text=True)


def sed_docroot(domain, old_docroot, user='user'):
    command = f'grep -rl {old_docroot} /home/{user}/web/{domain}/public_html'
    result = subprocess.run(['bash', '-c', command], capture_output=True, text=True)
    number_of_files_found = result.stdout

def sync_file():
    pass

def sync_dump():
    pass

def sed_db_access():
    pass

create_database('example.example.com')

print(type(create_pas()))