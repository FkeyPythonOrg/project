# Мои Проекты

Коллекция веб-проектов и Python-приложений.

## Структура проекта

```
project/
├── web/                    # Веб-проекты
│   ├── index.html          # Главная страница
│   ├── css/
│   │   └── style.css       # Стили
│   ├── js/
│   │   └── script.js       # Скрипты
│   └── templates/          # HTML шаблоны
│       ├── site.html       # Шаблон сайта компании
│       ├── support.html    # Шаблон страницы поддержки
│       └── clicker.html    # Игра-кликер
│
├── python/                 # Python-проекты
│   ├── lemonade_tycoon.py # Игра "Lemonade Tycoon"
│   ├── mobil_gen.py        # Генератор мобильных номеров
│   └── requirements.txt    # Зависимости
│
└── docs/                   # Документация
    └── README.md           # Этот файл
```

## Запуск веб-проектов

1. Откройте `web/index.html` в браузере
2. Или используйте локальный сервер:
   ```bash
   cd web
   python -m http.server 8000
   ```
3. Откройте http://localhost:8000

## Запуск Python-проектов

1. Установите зависимости:
   ```bash
   cd python
   pip install -r requirements.txt
   ```

2. Запустите нужное приложение:
   ```bash
   # Lemonade Tycoon
   python lemonade_tycoon.py

   # Генератор номеров
   python mobil_gen.py
   ```

## Используемые технологии

- **Веб**: HTML5, CSS3, JavaScript
- **Python**: customtkinter

## Автор

Fkey
