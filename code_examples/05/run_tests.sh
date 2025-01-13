#! /bin/bash -eu

python graph.py
python count_authors.py
python typeddict.py
python reverse.py
python generic.py
python overriding_dict.py
python userdict.py
python abc.py

mypy *.py

# for f in code_examples/05/invalid/*
# do
# 	if mypy "$f" ; then
# 		echo "Expected $f to fail, but passed"
# 		exit 1;
# 	fi
# done
