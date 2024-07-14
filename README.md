Для клонирования репозитория
```
git clone https://github.com/Nauryeasy/UserAuthTest.git
```

Установка make
```
apt install make
```

После этого необходимо создать виртуальную среду Python.


Установка poetry
```
pip install poetry
```

Далее необходимо установить зависимости
```
poetry install
```

После этого нужно либо переименовать .env.example в .env, либо создать .env по подобию .env.example.

Для запуска приложения
```
make app
```

После запуска необходимо сделать миграции
```
make migrations
make migrate
```

Для создания супер пользователя (Необходимо для тестирования некоторых методов API)
```
make superuser
```

Для логов приложения
```
make app-logs
```

Для создания пользователя нужно отправить POST запрос по эндпоинту:
```
http://127.0.0.1:8000/api/auth/users/
```
с телом:
{
	"username": "name_user",
	"email": "email_user",
	"password": "password_user"
}

Для авторизации можно отправлять заголовок Authorization со значением Basic имя пользователя и пароль в Base64, либо получить JWT токен по эндпоинту:
```
http://127.0.0.1:8000/api/auth/jwt/create/
```
с телом:
{
	"username": "name_user",
	"password": "password_user"
}
и передавать его в заголовке Authorization в формате Bearer access _token

Для изменения данных о пользователе (нужна авторизация) необходимо отправить PUT запрос на эндпоинт:
```
http://127.0.0.1:8000/api/auth/users/me/
```
где в теле будут ключами поля, которые необходимо изменить, а значениями будут новые значения для этих полей. (Нельзя изменить password и username)

Для изменения пароля нужно отправить  POST запрос на эндпоинт (нужна авторизация):
```
http://127.0.0.1:8000/api/auth/users/set_username/
```
с телом:
{
    "current_password": "password_user",
    "new_username": "new_name_user"
}

Для изменения username нужно отправить  POST запрос на эндпоинт (нужна авторизация):
```
http://127.0.0.1:8000/api/auth/users/set_password/
```
с телом:
{
    "new_password": "new_password",
    "current_password": "old_password"
}

Для удаления пользователя нужно отправить DELETE запрос на эндпоинт (нужна авторизация):
```
http://127.0.0.1:8000/api/auth/users/me/
```

Для просмотра списка пользователей нужно отправить запрос на эндпоинт (нужна авторизация от лица супер пользователя):
```
http://127.0.0.1:8000/api/auth/users/
```
