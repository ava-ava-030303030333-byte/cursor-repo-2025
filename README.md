# Чатбот регистрации на мероприятие

Проект Python чатбота для регистрации участников на мероприятие.

## Функционал

- Собирание данных: ФИО, email, телефон, название организации
- Валидация email и телефона
- Сохранение регистраций в JSON файл
- Два модуля: консоль и Telegram бот

## Архитектура проекта

```
event_registration_bot/
├── config/
│   └── settings.py          # Настройки приложения
├── data/
│   └── registrations.json   # JSON файл с регистрациями
├── models/
│   └── registration.py      # Модель данных регистрации
├── validators/
│   └── validators.py       # Функции валидации
├── storage/
│   └── json_storage.py     # Сохранение в JSON
├── interfaces/
│   ├── console_interface.py # Консоль
│   └── telegram_bot.py     # Telegram бот
├── requirements.txt     # Зависимости
├── main.py              # Маин-скрипт
└── README.md
```

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

На консоли:
```bash
python main.py
```

На Telegram (нужно указать токен в .env ныли в config/settings.py):
Выберите опцию 2 в меню

## Копирайт

Чатбот регистрации на мероприятие. 2025.

## Админ-меню

Для доступа к админ-меню:
- Выберите опцию 3 в главном меню
- Введите пароль: **1234**
- На консоли: команда 'admin' в меню
- На Telegram: команда '/admin'

В админ-меню можно:
- Посмотреть статистику (всего регистраций, размер БД)
- На консоли: 1 - все данные
- Цию: '0' для выхода

## Архитектура с Mermaid диаграммой

```mermaid
graph TD
    U[키Оприятие] -->|Через Telegram| B[탒Отелеграм Bot Interface]
    U -->|Через терминал| C[탈Консоль Interface]
    A[А дминистратор] -->|1. Команда 'admin' в консоли| AC[ОАдмин-консоль]
    A -->|2. Команда /admin в Telegram| AT[АТАдмин-Телеграм]
    B --> MAIN[ММАНИ МОеню]
    C --> MAIN
    AC --> MAIN
    AT --> MAIN
    MAIN -->|Лаунч режим| Reg[РРЕГИСТАЦИЙ]
    MAIN -->|Админ режим| Admin[ААдмин Панель]
    Reg -->|Ввод данных| FSM[РОНОТОТО FSM режим]
    FSM -->|Чита/Пишет| Storage[탍Хранилище данных]
    Admin -->|Чита/Пишет| Storage
    Admin -->|Просмотр номер| Stat[탒Статистика]
    Storage -->|JSON файл| DB[탒registrations.json]
    Config[탒Конфигурация] -->|параметры| MAIN
    Config -->|путь к JSON| Storage
```
