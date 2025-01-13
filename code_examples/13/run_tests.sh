#! /bin/bash -eu

python splittable.py
python splittable_inheritance.py
python iterator.py
python splittable_protocol.py
python runtime_checking.py
python load_restaurant.py

mypy *.py
