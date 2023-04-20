import os
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice
from aiogram.types import ContentType
from Keyboards.Callback import course_navigation
from loader import dp, lecture_db
from Misc import MsgToDict, Lecture


@dp.callback_query_handler(course_navigation.filter(menu='purchase'))
async def purchase(msg: MsgToDict):
    target_lecture = Lecture(lecture_db.select(msg.table, msg.id))
    prices = [LabeledPrice(label=f'{target_lecture.name}', amount=target_lecture.price*100)]

    await dp.bot.send_invoice(chat_id=msg.my_id,
                              title='Оплата лекции!',
                              description='Подтвердите выбор лекции',
                              provider_token=os.getenv('P_TOKEN'),
                              currency='RUB',
                              prices=prices,
                              payload=f'{msg.table}:{msg.id}',
                              start_parameter='purchase')
@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: Message, msg: MsgToDict):
    my_purchase = message.successful_payment.invoice_payload
    lecture_db.purchase(msg.my_id, *my_purchase.split(':'))
    await message.answer(text='Спасибо за покупку!\nДоступ к лекции будет в главном меню')