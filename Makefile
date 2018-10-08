run:
	flask run

kill:
	sudo lsof -i tcp:5000

development:
	export FLASK_ENV=development

logs:
	mkdir logs
	touch errors.log
	touch debug.log
	touch warning.log
	touch critical.log

db_init:
	flask db init

db_migrate:
	flask db migrate

db_upgrade:
	flask db upgrade