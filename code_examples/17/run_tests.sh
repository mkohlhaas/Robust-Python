#! /bin/bash -eu

python call_repeat.py
python recommendation.py
python recommendation_improved.py

mypy *.py
