# Учебный проект по Python для фильтрации и сортировки банковских операций.

## 📦 Установка и запуск

1. Клонируйте репозиторий:
```
git clone https://github.com/vadiaanx/bank_project.git
```
2. Установите Poetry, если он ещё не установлен:
```
curl -sSL https://install.python-poetry.org | python3 -
```

3. Установите зависимости:
```
poetry install
```
4. Активируйте виртуальное окружение:
```
poetry shell
```
5. Запустите основной скрипт:
```
python src/main.py
```

## ✅ Проверка качества кода
### Для проверки качества кода используются:
* flake8
* mypy
* black
* isort

### Команды для запуска:
```
flake8 .
mypy .
black .
isort .
```