from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.storage.memory import MemoryStorage

from data_from_sofascore.online import online_list
from data_from_sofascore.today import today_list
from keyboards.keyboard import create_kb1, kb_info, kb_tournament_tables, kb_back_menu, kb_profile
from data_from_sofascore.tournament_tables import about, epl_tournament_table, laliga_tournament_table, bundesliga_tournament_table, \
    seriea_tournament_table, ligaone_tournament_table, rpl_tournament_table
from db.requests import set_user, add_data, get_info, add_email

storage = MemoryStorage()



user_dict: dict[int, dict[str, str | int | bool]] = {}

user_router = Router()


class FSMEditProfile(StatesGroup):
    waiting_for_name = State()
    waiting_for_email = State()


@user_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("SELECT ITEM", reply_markup=create_kb1())


@user_router.callback_query(F.data == 'info')
async def start_info(callback: CallbackQuery):
    await callback.message.answer(text="Select Item ... ⏳", reply_markup=kb_info())
    await callback.answer(text='Информационный раздел')


@user_router.callback_query(F.data == 'interactive')
async def interactive(callback: CallbackQuery):
    await set_user(callback.from_user.id)
    await callback.message.answer(text="Добро пожаловать!", reply_markup=kb_profile())


@user_router.message(F.text == 'profile')
async def get_profile(message: Message):
    profile = await get_info(message.from_user.id)
    await message.answer(text=profile, reply_markup=ReplyKeyboardRemove())


@user_router.message(F.text == 'edit profile', StateFilter(default_state))
async def edit_profile(message: Message, state: FSMContext):
    await message.answer('Укажите ваше имя')
    await state.set_state(FSMEditProfile.waiting_for_name)


@user_router.message(StateFilter(FSMEditProfile.waiting_for_name))
async def process_name(message: Message, state: FSMContext):
    new_name = message.text
    await add_data(message.from_user.id, new_name)
    await message.reply("Новое имя сохранено\nВведите email:")
    await state.set_state(FSMEditProfile.waiting_for_email)


@user_router.message(StateFilter(FSMEditProfile.waiting_for_email))
async def process_mail(message: Message, state: FSMContext):
    email = message.text
    await add_email(message.from_user.id, email)
    await message.reply("email saved")
    await state.clear()


#
#
#     new_name = ?
#     await add_data(message.from_user.id, new_name)
#     await message.reply(text="Данные сохранены")
#     data = await get_info(message.from_user.id)
#     await message.answer(text=data, reply_markup=ReplyKeyboardRemove())







#     await callback.message.answer(text="введите имя")
#
#
# @user_router.message()
async def add_name(message: Message):
    await add_data(message.from_user.id, message.text)
    await message.answer("Данные внесены")
    info = await get_info(message.from_user.id)
    await message.answer(text=info)




    #
    # # await callback.message.answer_sticker(sticker='CAACAgIAAxkBAAEJD-BnBo4XwXrgvsA17IeVFyzEOkIAAc8AAmEJAAJAjVlL8oFCIj1C1os2BA', reply_markup=create_kb1())
    # await callback.answer('unavailable')


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


@user_router.callback_query(F.data == 'online')
async def online_list_table(callback: CallbackQuery):
    await callback.message.answer(text=online_list(), reply_markup=kb_back_menu(), parse_mode='HTML')
    await callback.answer()


@user_router.callback_query(F.data == 'today')
async def today_list_table(callback: CallbackQuery):
    await callback.message.answer(text=today_list(), reply_markup=kb_back_menu())
    await callback.answer()






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
