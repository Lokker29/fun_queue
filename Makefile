.DEFAULT_GOAL = run

build:
	docker build --tag fun_queue_web .


run:
	docker-compose up -d


stop:
	docker-compose stop

mm:
	docker exec -it fun_queue_web_1 python manage.py migrate


mkm:
	docker exec -it fun_queue_web_1 python manage.py makemigrations
