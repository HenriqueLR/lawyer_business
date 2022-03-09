#!/bin/bash -xe

nginx_run(){
	sudo cp ./env/nginx/default /etc/nginx/sites-enabled/default;
	sudo /etc/init.d/nginx restart;		
	return 0;
}

postgresql_run(){
	sudo /etc/init.d/postgresql restart;
	/bin/bash
	return 0;
		
}

supervisord_run(){
	supervisord -c /etc/supervisord/supervisord.conf
	supervisorctl restart all;	
	return 0;
}

django_run(){
	./app/manage.py collectstatic --noinput;
	find . -name "*.sqlite3" | xargs rm -f;
	find . -name "*.pyc" | xargs rm -f;
	./app/manage.py makemigrations --settings=conf.settings_production;
	./app/manage.py migrate --settings=conf.settings_production;
	return 0;
}

app(){
	django_run;
	supervisord_run;
	nginx_run;
	return 0;
}

bd(){
	postgresql;
	return 0;
}

$1

/bin/bash