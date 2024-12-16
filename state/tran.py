from aiogram.fsm.state import StatesGroup, State


class TranState(StatesGroup):
    token = State()
    amount = State()
    note = State()


print()