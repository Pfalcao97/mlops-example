install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

run:
	uvicorn app:app --reload

format:
	black *.py

lint:
	pylint *.py