#! /bin/bash -eu

# PYTHONPATH=. python main.py
python main.py
mypy *.py
monkeytype run main.py
