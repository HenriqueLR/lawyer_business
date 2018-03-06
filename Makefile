#makefile
SHELL := /bin/bash


install: permissions
	pip install -r requirements.txt ;\
	./setup.sh ;\

runserver_prodution:
	./env/runserver.sh

runserver_local:
	python3.6 app/manage.py runserver 0.0.0.0:8001 --settings=conf.settings

connect_container:
	./env/connect-container.sh

collectstatic:
	python3.6 app/manage.py collectstatic

migrate:
	python3.6 app/manage.py makemigrations,migrate --settings=conf.settings ;\
	python3.6 app/manage.py makemigrations,migrate --settings=conf.settings_production ;\

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
	find . -name "*.sh" | xargs chmod 0755
