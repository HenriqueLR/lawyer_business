#!/bin/bash -xe

nginx_run(){
	sudo cp ./env/nginx/default /etc/nginx/sites-enabled/default;
	sudo /etc/init.d/nginx restart;		
}

postgresql_run(){
	sudo /etc/init.d/postgresql restart;
	/bin/bash
}

supervisord_run(){
	supervisord -c /etc/supervisord/supervisord.conf
	supervisorctl restart all;	
}

django_run(){
	./app/manage.py collectstatic --noinput;
	find . -name "*.sqlite3" | xargs rm -f;
	find . -name "*.pyc" | xargs rm -f;
	./app/manage.py makemigrations --settings=conf.settings_production;
	./app/manage.py migrate --settings=conf.settings_production;
}

app(){
	django_run;
	supervisord_run;
	nginx_run;
}

bd(){
	postgresql;
}

$1

/bin/bash