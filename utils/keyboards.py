from aiogram.types import InlineKeyboardButton as kb_btn
from aiogram.types import InlineKeyboardMarkup as kb_markup
from utils import settings
async def main_menu():
    keyboard = kb_markup(inline_keyboard=[
        [kb_btn(text=f'👤 Кабинет', callback_data='cabinet')],
        [kb_btn(text='❔ ЧаВо', callback_data='faq_bot')],
        [kb_btn(text='⚙️ Поддержка', url=f't.me/{settings.SUPPORT}')]])
    return keyboard

async def main_menuCabinet():
    keyboard = kb_markup(inline_keyboard=[
        [kb_btn(text=f'🚀 Вывести', callback_data='go_ref')],
        [kb_btn(text='👛 Пополнить', callback_data='blocked')],
        [kb_btn(text='🛍 Перейти в маркет', callback_data='blocked')],
        [kb_btn(text=f'<< Назад', callback_data='main_menu')]])
    return keyboard


async def format_nftBtn(uid: str, name: str):
    keyboard = kb_markup(inline_keyboard=[[
        kb_btn(text=f'🎁 Получить {name}', url=f'https://t.me/ntwlt_bot?start=nft{uid}')
    ]])
    print(len('https://t.me/ntwlt_bot?start={uid}'))
    return keyboard

async def main_menuRefferer():
    keyboard = kb_markup(inline_keyboard=[[
        kb_btn(text=f'⚡️ Посмотреть в меню', callback_data='main_menu')
    ]])
    return keyboard

async def back_menu():
    keyboard = kb_markup(inline_keyboard=[[kb_btn(text=f'<< Назад', callback_data='main_menu')]])
    return keyboard
async def main_BotRefferer():
    keyboard = kb_markup(inline_keyboard=[[
        kb_btn(text=f'⚡️ Быстрая регистрация', url=f'{settings.REF_BOT}')],
        [kb_btn(text='✅ Регистрация пройдена', callback_data='check')]])
    return keyboard