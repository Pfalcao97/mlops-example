install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

run:
	uvicorn app:app --reload

format:
	black *.py

lint:
	pylint *.py

start-docker:
	systemctl --user start docker-desktop

delete-docker:
	docker image rm mlops-image 

create-docker:
	docker build -t mlops-image . 
	docker run -p 8000:8000 --rm --name mlops-container mlops-image 

docker:
	start-docker delete-docker create-docker