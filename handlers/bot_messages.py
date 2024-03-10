from aiogram import Router, F, types
from aiogram.types import Message
import text



from keyboards import reply
from utils.states import  Form

router = Router()




@router.message(F.text.lower() == "я человек")
async def with_puree(message: types.Message):
    await message.reply(text.average, reply_markup=reply.main_kb)




