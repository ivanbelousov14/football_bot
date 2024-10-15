from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_kb1():
    kb_builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text="📖 INFO", callback_data='info')
    button_2 = InlineKeyboardButton(text="🎲 INTERACTIVE", callback_data='interactive')
    button_3 = InlineKeyboardButton(text='😎 ABOUT ME', callback_data='about me')
    kb_builder.row(button_1, button_2, button_3, width=3)
    return kb_builder.as_markup()


def kb_back_menu():
    kb_builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text="⬅️ BACK", callback_data='back')
    button_2 = InlineKeyboardButton(text="▶️ MENU", callback_data='menu')
    kb_builder.row(button_1, button_2, width=3)
    return kb_builder.as_markup()

def kb_info():
    kb_builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text='Matches today', callback_data='today')
    button_2 = InlineKeyboardButton(text='Matches online', callback_data='online')
    button_3 = InlineKeyboardButton(text='Tournament tables', callback_data='tournament tables')
    # button_4 = InlineKeyboardButton(text='BACK', callback_data='back')
    kb_builder.row(button_1, button_2, button_3, width=3)
    return kb_builder.as_markup()


def kb_tournament_tables():
    kb_builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League', callback_data='england')
    button_2 = InlineKeyboardButton(text='🇪🇸 La Liga', callback_data='spain')
    button_3 = InlineKeyboardButton(text='🇩🇪 Bundesliga', callback_data='germany')
    button_4 = InlineKeyboardButton(text='🇮🇹 Serie A', callback_data='italy')
    button_5 = InlineKeyboardButton(text='🇫🇷 Ligue 1', callback_data='france')
    button_6 = InlineKeyboardButton(text='🇷🇺 RPL', callback_data='russia')
    # button_7 = InlineKeyboardButton(text='MENU', callback_data='back')

    kb_builder.row(button_1, button_2, button_3, button_4, button_5, button_6, width=3)
    return kb_builder.as_markup()


def kb_profile():
    button_1 = KeyboardButton(text='profile')
    button_2 = KeyboardButton(text='edit profile')
    kb = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True)
    return kb

