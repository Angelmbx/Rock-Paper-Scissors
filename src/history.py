from collections import Counter
from constants import GameAction, Victories
import random

user_history = [] # Lista en la cual se guardarán las elecciones del usuario

def update_user_history(user_action):

    user_history.append(user_action) # Añade la elección del usuario al historial


def predict_user_action():

    if not user_history:
        return random.choice(list(GameAction))  # Si el historial está vacío realiza una elección al azar

    # Analiza la elección preferida del usuario
    favourite_choice = Counter(user_history).most_common(1)[0][0]

    # Elige, dentro del diccionario Victories, la opción que contrarresta la elección favorita del jugador
    return Victories[favourite_choice]
