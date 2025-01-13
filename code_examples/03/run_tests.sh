#! /bin/bash -eu

python find_workers.py
python variable_annotation.py
python invalid/invalid_example1.py
python invalid/invalid_example2.py
python invalid/invalid_example3.py
python invalid/invalid_type.py

mypy *.py

for f in invalid/*
do
! mypy "$f" 2>/dev/null
done
