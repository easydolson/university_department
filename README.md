# Управление кафедрой университета

Django веб-приложение для информационной системы кафедры университета.

## Функционал
- Управление сотрудниками кафедры (25 человек)
- Учет ставок преподавателей
- Закрепление рабочих мест
- Ведение дисциплин
- Учет дополнительной работы (кураторство, практики, публикации)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/easydolson/university_department.git
cd university_department
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```

## Использование

- Главная страница: `http://127.0.0.1:8000/`
- Админ-панель: `http://127.0.0.1:8000/admin/`
- Список сотрудников: `http://127.0.0.1:8000/employees/`
- Список дисциплин: `http://127.0.0.1:8000/subjects/`

## Структура проекта

```
university_department/
├── department/          # Основное приложение
├── university_department/  # Настройки проекта
├── manage.py           # Управление Django
└── requirements.txt    # Зависимости
```