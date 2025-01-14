#! /bin/bash -eu

python types_example.py
python memory_value.py
python double_items.py

# just prints out
python print_items.py

mypy *.py
