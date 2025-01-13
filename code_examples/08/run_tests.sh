#! /bin/bash -eu

python mother_sauces_bad.py
python mother_sauces.py
python auto_enum.py
python auto_enum_generate.py
python allergen.py
python allergen_flag.py
python liquid_measure.py
python liquid_measure_intenum.py
python mother_sauces_alias.py
python mother_sauces_unique.py

mypy *.py
