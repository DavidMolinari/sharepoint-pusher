VENV=.venv

setup:
	uv venv $(VENV)
	uv pip install -r requirements.txt --python $(VENV)/bin/python

run:
	$(VENV)/bin/uv -m news_poster.cli $(ARGS)

test:
	$(VENV)/bin/uv -m pytest -v

.PHONY: setup run test
