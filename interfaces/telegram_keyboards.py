# interfaces/telegram_keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню с 4 кнопками"""
    keyboard = [
        [KeyboardButton(text="📝 Рег")],
        [KeyboardButton(text="🔑 Логин")],
        [KeyboardButton(text="📋 Мероприятия")],
        [KeyboardButton(text="⚙️ Админ")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выберите действие..."
    )

def get_events_list_keyboard(events: list) -> InlineKeyboardMarkup:
    """Динамическая клавиатура списка мероприятий"""
    buttons = []
    for event in events:
        buttons.append([
            InlineKeyboardButton(
                text=event["name"],
                callback_data=f"event_register_{event['id']}"
            )
        ])
    
    buttons.append([
        InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура подтверждения"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Да", callback_data="confirm_yes"),
            InlineKeyboardButton(text="❌ Нет", callback_data="confirm_no")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")
        ]
    ])

def get_back_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с кнопкой 'Назад'"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ])
