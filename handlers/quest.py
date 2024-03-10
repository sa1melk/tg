from aiogram import Router, types, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.methods.send_message import SendMessage
from aiogram.methods import SendMessage
from datetime import datetime, timedelta
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import Filter
from utils.states import Form
from utils.states import AdminReplyState
import text
from aiogram.types import CallbackQuery
from aiogram import F
from config_reader import config
import random





bot=Bot(config.bot_token.get_secret_value())
router = Router()




# хранилище данных
user_last_request = {}

wishes = [
    "Желаем вам отличного дня!",
    "Пусть этот день принесет только радость!",
    "Сегодня вас ждут только приятные сюрпризы!",
    "Желаю сегодня замечательного, волшебного настроения",
    "Наступил новый день, он несет в себе что-то неожиданное",
    "Пусть хороший, добрый, веселый день ждет тебя сегодня",
    "Чтобы твой день сегодня с каждым часом становился всё лучше",
    "Пусть наступающий день будет ярким, полным приятных эмоций и светлых идей",
    "Каждый новый день таит в себе какую-то изюминку",
    "Пусть наступивший день будет наполнен положительными эмоциями и великолепным настроением",
    "От души желаю приятного, успешного и хорошего дня",
    "Желаю огромной удачи на сегодня и в целом хорошего дня.",
    "Пусть сегодняшний день обернется беззаботным весельем и невероятным счастьем",

    
]



@router.message(F.text.lower() == "пожелание на день")
async def send_wish(message: types.Message):
    user_id = message.from_user.id
    current_time = datetime.now()

    # Проверяем, запрашивал ли пользователь пожелание сегодня
    if user_id in user_last_request and (current_time - user_last_request[user_id]).days < 1:
        await message.answer("Вы уже получили своё пожелание на сегодня! Попробуйте завтра :)")
        return

    # Обновляем время последнего запроса пожелания для пользователя
    user_last_request[user_id] = current_time

    # Отправляем рандомное пожелание из списка
    wish = random.choice(wishes)
    await message.answer(wish)










@router.message(F.text.lower() == "📨связь с админом")
async def process_message(message: Message, state: FSMContext):
    await state.set_state(Form.txt)
    await message.answer(text.connection)

def generate_reply_markup(user_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ответить', callback_data=f"reply_{user_id}")]
    ])
    


@router.message(Form.txt)
async def form_txt(message: Message, state: FSMContext, bot : Bot):
    await state.update_data(txt=message.text)
    await bot.send_message(
        config.ADMIN_CHAT_ID,
        f"Сообщение от пользователя {message.from_user.id}: {message.text}",
        reply_markup=generate_reply_markup(message.from_user.id)
    )
    await message.answer("Ваш вопрос отправлен техподдержке.")
    await state.clear()

@router.callback_query(F.data.startswith("reply_"))
async def process_reply_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.data.split("_")[1]
    await state.set_state(AdminReplyState.waiting_for_reply)
    await state.update_data(reply_to_user_id=user_id)
    await bot.send_message(chat_id=config.ADMIN_CHAT_ID, text="Введите ответ пользователю:")




@router.message(AdminReplyState.waiting_for_reply)
async def send_reply_to_user(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data['reply_to_user_id']
    await bot.send_message(chat_id=user_id, text=f"Ответ от админа: {message.text}")
    await bot.send_message(chat_id=config.ADMIN_CHAT_ID, text="Ответ успешно отправлен.")
    await state.clear()






@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == '🚫отключить рекламу':
       await message.answer(text.advertising)