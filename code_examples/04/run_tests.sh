#! /bin/bash -eu

python create_hot_dog.py
python create_hot_dog_defensive.py
python create_hot_dog_union.py
python product_type.py
python sum_type.py
python invalid/dispense_bun.py
python invalid/hotdog_invalid.py
python invalid/union_hotdog.py
python invalid/literals.py
python invalid/final.py
python invalid/newtype.py

mypy *.py

# for f in invalid/*
# do
# ! mypy "$f" 2>/dev/null
# done
