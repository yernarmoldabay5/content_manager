from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

row = 1
keyboard = []

keyboard.append(InlineKeyboardButton(text="Одобрить", callback_data="Y"))
keyboard.append(InlineKeyboardButton(text="Отказать", callback_data="N"))

choice = InlineKeyboardMarkup(row_width=2, inline_keyboard=
[
    [InlineKeyboardButton(text="Одобрить", callback_data="Y"),
     InlineKeyboardButton(text="Отказать", callback_data="N")
     ]
]
                              )
