<h1> 🚗 Зпуск приложения: </h1>


`git clone https://github.com/Alexmdvdv/library_drf.git`

`docker-compose build`

`docker-compose up`



<h1> ✉️ Проверка письма: </h1>

> `https://mailtrap.io/inboxes` - нужен VPN!

> Логин: `vayelek779@nasmis.com`

> Пароль: `test12test`




<h1> 🧐 Как пользоваться: </h1>

### GET: book/library/int/:

```
Response: 

{
    "title": "<title>",
    "authors": "<authors>",
    "year_publication": "<year_publication>",
    "isbn": "<isbn>"
}
```

### PATCH: book/library/int/:

```
Request: 

{
    "title": "<title>",
}
```

```
Response: 

{
    "title": "<title>",
    "authors": "<authors>",
    "year_publication": "<year_publication>",
    "isbn": "<isbn>"
}

```

### DELETE: book/library/int/:

```
Требуется указать id записи
```

### GET: book/library/

```
Response: 

[
    {
        "title": "<title>",
        "authors": "<authors>",
        "year_publication": "<year_publication>",
        "isbn": "<isbn>"
    },
]
```

### POST: book/library/

```
Request:

{
    "title": "<title>",
    "authors": "<authors>",
    "year_publication": "<year_publication>",
    "isbn": "<isbn>"
}
```

### POST: user/register/

```
Request:

{
    "username": "<username>", 
    "email": "<email>",
    "password": "<password>"

}
```

```
Response:

{
    "username": "<username>", 
    "email": "<email>",
    "refresh": "<refresh_token>",
    "access": "<access_token>"

}

```



