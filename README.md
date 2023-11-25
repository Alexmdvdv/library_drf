### 🚗 Зпуск приложения::


`git clone https://github.com/Alexmdvdv/library_drf.git`

`docker-compose build`

`docker-compose up`

### ✉️ Для проверки письма на почте:
`https://mailtrap.io/inboxes` - нужен VPN!

Логин:
`vayelek779@nasmis.com`

Пароль: `test12test`


### 🧐 Как пользоваться:

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

### GET: book/reader/int/

```
Response:

{
    "username": "<username>", 
    "email": "<email>"

}
```

### GET: book/reader/

```
Request:

{
    "username": "<username>", 
    "email": "<email>"

}
```


