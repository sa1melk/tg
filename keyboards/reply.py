from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import Message
from aiogram import Bot, Dispatcher, Router, types

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Я человек")
        ],
    ],
    resize_keyboard=True
        
)
      
    


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пожелание на день"),
        ],
        [
            KeyboardButton(text="📨Связь с админом"),
        ],
        [
            KeyboardButton(text="🚫Отключить рекламу"),
        ]
    ],
    resize_keyboard=True,
    selective=True
)