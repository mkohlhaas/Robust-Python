#! /bin/bash -eu

python adjust_recipe.py
python adjust_recipe_wrong.py
python adjust_recipe_improved.py
python cookbooks.py
python cookbooks_counter.py
python cookbooks_defaultdict.py
python iteration.py

mypy *.py
