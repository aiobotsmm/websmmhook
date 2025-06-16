from aiogram.fsm.state import StatesGroup, State

class Register(StatesGroup):
    name = State()
    phone = State()

class AddBalance(StatesGroup):
    amount = State()
    txn_id = State()
