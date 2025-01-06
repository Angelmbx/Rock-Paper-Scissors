import pytest
from src.game_logic import assess_game
from src.constants import GameAction, GameResult

def test_assess_game_rock_vs_scissors():
    result = assess_game(GameAction.Rock, GameAction.Scissors)
    assert result == GameResult.Victory  # Piedra gana a Tijera

def test_assess_game_scissors_vs_paper():
    result = assess_game(GameAction.Scissors, GameAction.Paper)
    assert result == GameResult.Victory  # Tijera gana a Papel

def test_assess_game_paper_vs_rock():
    result = assess_game(GameAction.Paper, GameAction.Rock)
    assert result == GameResult.Victory  # Papel gana a Piedra

def test_assess_game_rock_vs_paper():
    result = assess_game(GameAction.Rock, GameAction.Paper)
    assert result == GameResult.Defeat  # Piedra pierde contra Papel

def test_assess_game_scissors_vs_rock():
    result = assess_game(GameAction.Scissors, GameAction.Rock)
    assert result == GameResult.Defeat  # Tijeras pierde contra Piedra

def test_assess_game_paper_vs_scissors():
    result = assess_game(GameAction.Paper, GameAction.Scissors)
    assert result == GameResult.Defeat  # Papel pierde contra Tijeras

def test_assess_game_tie():
    result = assess_game(GameAction.Rock, GameAction.Rock)
    assert result == GameResult.Tie  # Empate si ambos eligen Piedra

    result = assess_game(GameAction.Paper, GameAction.Paper)
    assert result == GameResult.Tie  # Empate si ambos eligen Papel

    result = assess_game(GameAction.Scissors, GameAction.Scissors)
    assert result == GameResult.Tie  # Empate si ambos eligen Tijeras
