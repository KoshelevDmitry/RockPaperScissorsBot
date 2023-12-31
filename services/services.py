import random
from lexicon.lexicon_ru import LEXICON_RU


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normaloze_user_answer(user_ansver: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_ansver:
            break
    return key


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normaloze_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
