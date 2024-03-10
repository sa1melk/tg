from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Form(StatesGroup):
    txt = State()



class AdminReplyState(StatesGroup):
    waiting_for_reply = State()