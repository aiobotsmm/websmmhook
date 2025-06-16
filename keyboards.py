from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu(balance=0):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 My Wallet")],
            [KeyboardButton(text="📥 New Order")],
            [KeyboardButton(text="📦 My Orders")],
        ],
        resize_keyboard=True
    )
