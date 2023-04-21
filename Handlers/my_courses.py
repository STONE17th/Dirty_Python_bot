from aiogram.types import InputMediaPhoto, CallbackQuery

from Keyboards import create_ikb_my_courses, create_ikb_my_course_navigation
from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course, Lecture, pictures
from loader import dp, bot, course_db, lecture_db, user_db


@dp.callback_query_handler(main_menu.filter(button='my_courses'))
async def check_course_or_lecture(call: CallbackQuery, msg: MsgToDict):
    courses, lectures = user_db.course_and_lectures(msg.my_id)
    print(courses)
    print(lectures)
    # print(course_db.select(table=course))
    # print(lecture_db.select(table, index))
    courses_list = [Course(course_db.select(table=course)) for course in courses.split()]
    lectures_list = [Lecture(lecture_db.select(lectures.split(':')[0], int(lectures.split(':')[1]))) for lectures in lectures.split()]
    print(courses_list)
    print(lectures_list)
    print('Стоп')
    poster = pictures.my_courses
    # desc = f'{msg.name}, это твои курсы!' if courses or lectures else f'{msg.name}, у тебя нет активных курсов!'
    # await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
    #                              chat_id=msg.chat_id, message_id=msg.message_id,
    #                              reply_markup=create_ikb_my_courses(courses, lectures, msg.my_id))

#
# @dp.callback_query_handler(course_navigation.filter(menu='my_courses'))
# async def users_courses(msg: MsgToDict):
#     courses = Course(course_db.whole(msg.table))
#     poster = courses.classes[msg.id].poster
#     desc = f'{msg.id + 1}/{courses.size}\n{courses.lecture(msg.id, True)}'
#     await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
#                                  chat_id=msg.chat_id, message_id=msg.message_id,
#                                  reply_markup=create_ikb_my_course_navigation('my_courses', msg.id, courses.size,
#                                                                               msg.table))
#
#
# @dp.callback_query_handler(course_navigation.filter(menu='my_lectures'))
# async def users_lectures(msg: MsgToDict):
#     lectures = Course(lecture_db.users(msg.my_id))
#     poster = lectures.classes[msg.id].poster
#     desc = f'{msg.id + 1}/{lectures.size}\n{lectures.lecture(msg.id, True)}'
#     await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
#                                  chat_id=msg.chat_id, message_id=msg.message_id,
#                                  reply_markup=create_ikb_my_course_navigation('my_lectures', msg.id, lectures.size))
