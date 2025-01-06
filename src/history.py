from collections import Counter, defaultdict
from constants import GameAction, Victories
import random

user_history = [] # Lista en la cual se guardarán las elecciones del usuario
next_move = defaultdict(lambda: defaultdict(int)) # diccionario en el que se guardarán la secuencia de elecciones


# Actualiza la secuencia de elecciones con la selección actual del jugador
def update_next_move(previous_action, current_action):
    next_move[previous_action][current_action] += 1 


def update_user_history(user_action):
    if user_history:
        update_next_move(user_history[-1], user_action) # Actualiza la secuencia de elecciones

    user_history.append(user_action) # Añade la elección del usuario al historial


# Predice la acción del jugador combinando su acción favorita e historial de secuencia de elecciones. Además añade un pequeño factor de aleatoriedad
def predict_user_action():
    # Si no hay historial elige al azar
    if not user_history:  
        return random.choice(list(GameAction))
    
    # 1. Predicción basada en historial de secuencias
    last_action = user_history[-1] 
    next_action_probabilities = next_move[last_action]


    if next_action_probabilities:
        predicted_by_sequence = max(next_action_probabilities, key=next_action_probabilities.get)
    else:
        predicted_by_sequence = None

    # 2. Predicción basada en la elección favorita del jugador
    favourite_choice = Counter(user_history).most_common(1)[0][0]

    # 3. Combina las dos predicciones
    # Si hay datos sobre el historial de secuencias se le da prioridad a esta predicción. Si no se detecta un patrón claro elige como predicción la acción favorita del jugador
    if predicted_by_sequence: 
        predicted_next = predicted_by_sequence
    else:
        predicted_next = favourite_choice

    
    # Elige, dentro del diccionario Victories, la opción que contrarresta la predicción de elección del jugador
    predicted_counter = Victories[predicted_next]

    # 4. Introduce aleatoriedad en un pequeño porcentaje para evitar que el jugador detecte patrones en la elección del agente
    if random.random() < 0.8:  # 80% probabilidad de elegir la contraria
        return predicted_counter
    else:  # 20% probabilidad de elegir al azar
        return random.choice(list(GameAction))
