# Мини проект на  Django 

## Задание:

Создать проект на Django. 
Путь update_autoru_catalog должен собрать с каталога авто.ру марки и модели автомобилей и занести в базу данных.

В базе данных нужны 2 модели: Марка и Модель. У Модели должен быть внешний ключ на Марку.
Базу достаточно на sqlite сделать.
При каждом вызове update_autoru_catalog удалять прошлые данные из базы и загружать новые.

Значение Марки брать из тега mark, атрибута name.

Значение Модели брать из тега folder, атрибута name.

