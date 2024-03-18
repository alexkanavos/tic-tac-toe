import random


PLAYERS = ["X", "O"]


def choose_first_player() -> str:
    first_player = random.choice(PLAYERS)
    return first_player


def switch_player(player: str) -> str:
    for item in PLAYERS:
        if item != player:
            next_player = item
    return next_player
