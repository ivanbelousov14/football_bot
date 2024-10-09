import asyncio
from aiogram import Router, F
from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards.keyboard import create_kb1, kb_info, kb_tournament_tables, kb_back_menu
from data import about, epl_tournament_table, laliga_tournament_table, bundesliga_tournament_table, \
    seriea_tournament_table, ligaone_tournament_table, rpl_tournament_table

storage = MemoryStorage()

user_dict: dict[int, dict[str, str | int | bool]] = {}

user_router = Router()


class FSMmy(StatesGroup):
    enter_action = State()
    enter_info_action = State()
    enter_league = State()
    enter_matches = State()


@user_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("start", reply_markup=create_kb1())



@user_router.callback_query(F.data == 'info')
async def start_info(callback: CallbackQuery):
    await callback.message.answer(text="Select Item ... ⏳", reply_markup=kb_info())
    await callback.answer(text='Информационный раздел')


@user_router.callback_query(F.data == 'interactive')
async def interactive(callback: CallbackQuery):
    await callback.message.answer_sticker(sticker='CAACAgIAAxkBAAEJD-BnBo4XwXrgvsA17IeVFyzEOkIAAc8AAmEJAAJAjVlL8oFCIj1C1os2BA', reply_markup=create_kb1())
    await callback.answer('unavailable')


@user_router.callback_query(F.data == 'about me')
async def about_me(callback: CallbackQuery):
    await callback.message.answer(text=about, reply_markup=create_kb1())
    await callback.answer(text='description')
    await callback.answer()


@user_router.callback_query(F.data == 'tournament tables')
async def league_list(callback: CallbackQuery):
    await callback.message.answer(text="Турнирные таблицы", reply_markup=kb_tournament_tables())
    await callback.answer()


@user_router.callback_query(F.data == 'england')
async def epl_table(callback: CallbackQuery):
    await callback.message.answer(text=epl_tournament_table(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data == 'spain')
async def laliga_table(callback: CallbackQuery):
    await callback.message.answer(text=laliga_tournament_table(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data == 'germany')
async def bundesliga_table(callback: CallbackQuery):
    await callback.message.answer(text=bundesliga_tournament_table(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data == 'italy')
async def seriea_table(callback: CallbackQuery):
    await callback.message.answer(text=seriea_tournament_table(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data == 'france')
async def ligaone_table(callback: CallbackQuery):
    await callback.message.answer(text=ligaone_tournament_table(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data == 'russia')
async def ligaone_table(callback: CallbackQuery):
    await callback.message.answer(text=rpl_tournament_table(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data.in_(['back', 'menu']))
async def back_to(callback: CallbackQuery):
    if 'menu' in callback.data:
        await command_start(callback.message)
        await callback.answer()
    elif 'back' in callback.data:
        await callback.answer()
        await callback.message.delete()
        await callback.answer(reply_markup=None)




# @user_router.callback_query(F.data == 'back')
# async def back_to(callback: CallbackQuery):
#     # await callback.message.delete() #qweqwe
#     await league_list(callback)
#     await callback.answer()


#
# @user_router.message(Command('cancel'), ~StateFilter(default_state))
# async def command_cancel(message: Message, state: FSMContext):
#     await message.answer('вы вышли из машины состояний')
#     await state.clear()
#
#
