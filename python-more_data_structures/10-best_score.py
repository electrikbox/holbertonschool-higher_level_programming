#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None

    winner = None

    for key, value in a_dictionary.items():
        if winner is None or value > a_dictionary[winner]:
            winner = key

    return winner
