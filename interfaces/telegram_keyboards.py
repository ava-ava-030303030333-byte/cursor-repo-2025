from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Основное меню с кнопками внизу экрана"""
    keyboard = [
        [KeyboardButton(text="✅ Начать")],
        [KeyboardButton(text="🔧 Админ-панель")],
        [KeyboardButton(text="⏹ Отмена")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выберите действие..."
    )

def get_admin_menu_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура админ-меню"""
    keyboard = [
        [KeyboardButton(text="📊 Статистика")],
        [KeyboardButton(text="📋 Список участников")],
        [KeyboardButton(text="📁 Информация о файле")],
        [KeyboardButton(text="🚪 Выйти из админки")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )

def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    """Inline-кнопки для подтверждения регистрации"""
    keyboard = [
        [
            InlineKeyboardButton(text="✅ Да, подтверждаю", callback_data="confirm_yes"),
            InlineKeyboardButton(text="❌ Нет, отменить", callback_data="confirm_no")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_cancel_only_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура только с кнопкой отмены"""
    keyboard = [[KeyboardButton(text="⏹ Отмена")]]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )
