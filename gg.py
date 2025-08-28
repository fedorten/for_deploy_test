from random import randint
import random


def fight() -> str:
    player_hp = 10
    player_damage = randint(2, 5)
    enemy_hp = 15
    enemy_damage = randint(1, 3)

    while enemy_hp > 0 and player_hp > 0:
        enemy_hp -= player_damage
        player_hp -= enemy_damage
        print(f"{player_hp=}")
        print(f"{enemy_hp=}p")

    if enemy_hp < player_hp:
        print("победил игрок")
    else:
        print("вас победил бот азазазаза")


positive_answers = [
    "Да",
    "Безусловно",
    "Без сомнений",
    "Должно быть так",
    "Абсолютно точно",
    "Мне кажется, да",
    "Духи говорят да",
    "Очень вероятно",
    "Не сомневайтесь",
    "Определенно да",
    "Можешь быть уверен в этом",
]

negative_answers = [
    "Нет",
    "Не сейчас",
    "Не стоит",
    "Не надейтесь",
    "Не предвидится",
    "Лучше не спрашивать",
]

neutral_answers = [
    "Попробуйте позже",
    "Не уверен",
    "Нельзя сказать наверняка",
    "Скорее нет, чем да",
    "Всё зависит от обстоятельств",
    "Это сложный вопрос",
]

all_answers = [сюда свои предсказания]


def say_me_all():
    input("задай свой вопрос: ")
    answer = random.choice(all_answers)
    return answer


print(say_me_all())
