from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from keyboards import reply
import text

router = Router()





@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text.greetings, reply_markup=reply.menu_kb)