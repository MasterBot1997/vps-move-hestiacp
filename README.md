# Требование к серипту переноса.


#### Функции:
- `check_user`- Проверка пользователя
- `create_user` - Создание пользователя
- `check_database` - проверка есть ли БД уже для сайта и существует ли она
- `create_database` - создание и подключение БД к сайту
- `fix_permission` - корректировка прав доступа пользователя на дефолтные 755 и 644
- `sed_docroot` - функция седа старых путей
- `check_cms` - функция определения популярных cms - создать отдельный скрипт
- `create_pas` - функция генерации паролей, вспомогательная функция
- `sync_file` - rsync файлов
- `sync_dump` - rsync dump
- `sed_db_access` - седаем старые доступы
- 

---

#### Ключи передаваемые скрипту:

##### Обязательные:
- `-u user`
- `-h host`
- `-d docroot`
##### Опциональные:
- `--fix-permission`
- `--php-version`
- `--delete-old-file`
- `--php-mod`
- `--log-file`
- 

---

#### Описание функций:


Функция синка файлов `syn_file` будет использовать rsync. Из требований:
- Отключить проверку хэша хоста
- Должен хавать обязательные параметры `-docroot`, `-user`, `-host`
- Опциональный параметр `-pas`, если лень прокидывать ключ, что просто передадим его в rsync
> Нужно будет учесть что `-pas` пароль без ключа стоит прокидывать если уверен что там на сервере и перепроверять ничего не надо
