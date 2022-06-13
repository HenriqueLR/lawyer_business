#makefile
SHELL := /bin/bash

dmigrate:
	docker-compose exec app python app/manage.py makemigrations --settings=conf.settings_production;\
	docker-compose exec app python app/manage.py migrate --settings=conf.settings_production;\

remove_nginx:
	docker rm -f nginx

remove_postgresql:
	docker rm -f postgresql

remove_app:
	docker rm -f lawyer_business

restartall: remove_postgresql remove_app remove_nginx
	docker-compose up -d

remove:
	docker rm -f $(image);\

restart: remove
	docker-compose up --no-deps -d $(service);\

createsuperuser: $(image)
	docker-compose exec app python app/conf/config_init.py --conf production;\

build: permissions
	./setup.sh $(image) $(tag) $(service);\

dependences:
	pip install -r requirements.txt ;\

runserver_prodution: clean 
	./env/docker/runserver.sh $(image) $(tag) $(service) $(parent)

runserver_local: clean
	./app/manage.py runserver 0.0.0.0:8001 --settings=conf.settings

connect_container:
	./env/docker/connect-container.sh $(image)

collectstatic:
	./app/manage.py collectstatic --noinput ;\

migrate:
	./app/manage.py makemigrations --settings=conf.settings ;\
	./app/manage.py migrate --settings=conf.settings ;\

remove_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

doc:
	@sphinx-build -E -W -c docs/source/ -b html docs/source/ docs/build/html

clean:
	find . -name "*.pyc" | xargs rm -f

clean_db_local: remove_migrations clean
	find . -name "*.db" | xargs rm -f

reset_db_local: clean clean_db_local migrate

permissions:
	find . -name "*.sh" | xargs chmod 0755 ;\
