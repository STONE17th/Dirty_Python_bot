import os

from aiogram.types import ContentType
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, LabeledPrice

from Keyboards.Callback import course_navigation
from Misc import MsgToDict, Lecture, Course
from loader import dp, lecture_db, course_db


@dp.callback_query_handler(course_navigation.filter(menu='purchase'))
async def purchase(call: CallbackQuery, msg: MsgToDict):
    if msg.id == -1:
        target_lecture = Course(course_db.select(msg.table))
        merchandise = msg.table
    else:
        target_lecture = Lecture(lecture_db.select(msg.table, msg.id))
        merchandise = f'{msg.table}:{msg.id}'
    prices = [LabeledPrice(label=target_lecture.name, amount=target_lecture.price * 100)]

    await dp.bot.send_invoice(chat_id=msg.my_id,
                              title='Оплата лекции!',
                              description=target_lecture.name,
                              provider_token=os.getenv('P_TOKEN'),
                              currency='RUB',
                              prices=prices,
                              payload=merchandise,
                              start_parameter='purchase')


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: Message, msg: MsgToDict):
    my_purchase = message.successful_payment.invoice_payload
    if ':' in my_purchase:
        lecture_db.purchase(msg.my_id, *my_purchase.split(':'))
        text = 'лекции'
    else:
        course_db.purchase(msg.my_id, my_purchase)
        text = 'курсу'
    await message.answer(text=f'Спасибо за покупку!\nДоступ к {text} будет во вкладке "Мои курсы" /my_courses')
