.PHONY: run install clean

VENV_DIR ?= .env
PYTHON = python
REQUIREMENTS = requirements.txt

run:
	clear
	$(VENV_DIR)/bin/$(PYTHON) sterk.py

init:
	rm -rf $(VENV_DIR)
	@$(MAKE) $(VENV_DIR)

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

test:
	$(VENV_DIR)/bin/$(PYTHON) -m unittest discover

travis-install:
	pip install flake8

travis-test:
	python -m unittest discover

$(VENV_DIR):
	virtualenv $(VENV_DIR)
	if [ -a $(REQUIREMENTS) ] ; \
	then \
		$(VENV_DIR)/bin/pip install -r requirements.txt ; \
	else \
		$(VENV_DIR)/bin/pip install isort flake8 ; \
		$(VENV_DIR)/bin/pip freeze > requirements.txt ; \
	fi ;
