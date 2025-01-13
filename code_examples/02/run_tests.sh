#! /bin/bash -eu

python types_example.py
python memory_value.py
python double_items.py

# Just prints out - just grab errros
python print_items.py

mypy *.py
