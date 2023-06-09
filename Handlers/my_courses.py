from aiogram.types import InputMediaPhoto

from Keyboards import ikb_my_courses, ikb_my_course_navigation
from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course, PICTURES
from loader import dp, bot, course_db, user_db


@dp.callback_query_handler(main_menu.filter(button='my_courses'))
async def check_course_or_lecture(_, msg: MsgToDict):
    courses, lectures = user_db.course_and_lectures(msg.my_id)
    courses_list = [Course(course_db.select(table=course)) for course in courses.split()] if courses else []
    lectures_list = Course(
        (None, 'Отдельные лекции', 'custom', 'Лекции приобретенные поштучно', PICTURES.get('all_courses'),
         None, None, None, None, False))
    if lectures:
        [lectures_list.add_new(lecture) for lecture in lectures.split()]
    courses_list.append(lectures_list)

    poster = PICTURES.get('my_courses')
    desc = f'{msg.name}, это твои курсы!' if courses or lectures else f'{msg.name}, у тебя нет активных курсов!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=ikb_my_courses(courses_list))


@dp.callback_query_handler(course_navigation.filter(menu='my_courses'))
async def users_courses(_, msg: MsgToDict):
    if msg.table != 'custom':
        cur_course = Course(course_db.select(msg.table))
    else:
        _, lectures = user_db.course_and_lectures(msg.my_id)
        cur_course = Course((None, 'Отдельные лекции', 'custom', 'Лекции приобретенные поштучно',
                             None, None, None, None, None, 0))
        [cur_course.add_new(lecture) for lecture in lectures.split()]
    poster = cur_course.lectures[msg.id].poster if cur_course.lectures[msg.id].poster else PICTURES.get(
        'no_lecture')
    desc = f'{msg.id + 1}/{len(cur_course)}\n{cur_course.lecture(msg.id, False, True)}'
    buttons = (cur_course.lectures[msg.id].video, cur_course.lectures[msg.id].compendium)

    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=ikb_my_course_navigation('my_courses', buttons, msg.id,
                                                                       len(cur_course), msg.table))
