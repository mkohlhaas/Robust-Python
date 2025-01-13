#! /bin/bash -eu

python fraction.py
python recipe.py
python nutritional_info.py
python frozen_recipe.py
python namedtuple.py

mypy *.py
