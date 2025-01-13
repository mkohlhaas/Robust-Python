#! /bin/bash -eu

python person_construction.py
python pizza_maker.py
python pizza_maker_invariant.py
python pizza_maker_method.py

mypy *.py
