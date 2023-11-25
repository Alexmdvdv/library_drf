from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    year_publication = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)


class UserInfo(models.Model):
    """Не понял Часть 2 задание 1, создание модели пользователя с полями
    - Имя пользователя
    - Электронная почта
    - Дата регистрации
    т.к в стандартной модели пользователя уже имеются эти поля, оставил так, возможно это и имелось в виду"""
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    register_date = models.DateTimeField(auto_now_add=True)
