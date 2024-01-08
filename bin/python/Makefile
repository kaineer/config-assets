# bin/python/Makefile

prepare:
	pip install -r requirements.txt >../../log/python-prepare.log

test:
	PYTHONPATH=. pytest test

.PHONY: test
