from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_start_menu #, create_new_admin_confirm
import config
from data import counter
from Keyboards.Callback import main_menu, new_admin


# @dp.message_handler()
# async def start_command(message: Message, admin: bool):
#     print(admin)
#     # print(message.photo[0].file_id)

@dp.message_handler(commands=['start'])
async def start_command(message: Message, admin: bool):
    name = message.from_user.first_name
    poster = config.start_poster
    cur_chat = message.from_user.id
    cur_message = message.message_id
    if not db.check_user(cur_chat):
        db.new_user((cur_chat, name))
    description = f'Привет, {name}!'
    await bot.send_photo(chat_id=cur_chat, photo=poster,
                         caption=description, reply_markup=create_start_menu(admin))


@dp.callback_query_handler(main_menu.filter(button='back'))
async def start_command(call: CallbackQuery, admin: bool):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    if not db.check_user(cur_chat):
        db.new_user((cur_chat, name))
    description = f'Привет, {name}!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_start_menu(admin))


@dp.message_handler(content_types='photo')
async def request_to_admin(message: Message):
    print(message.photo[0].file_id)

# @dp.message_handler(commands=['admin_roots'])
# async def request_to_admin(message: Message):
#     for admin in config.admins_id:
#         await bot.send_message(chat_id=admin, text=f'{message.from_user.id} хочет в админы',
#                          reply_markup=create_new_admin_confirm(message.from_user.id))
#
# @dp.callback_query_handler(new_admin.filter(menu='new_admin'))
# async def add_new_admin(call: CallbackQuery):
#     if call.data.split(':')[-1] == 'yes':
#         config.admins_id.append(int(call.data.split(':')[-2]))
#         await call.answer(f'id {call.data.split(":")[-2]} добавлен в админы!', show_alert=True)
#         await bot.send_message(int(call.data.split(':')[-2]), 'Теперь ты админ!')
#     else:
#         await bot.send_message(int(call.data.split(':')[-2]), 'Соррян, тебе отказано')
