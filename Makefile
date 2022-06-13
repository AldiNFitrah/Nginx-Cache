all:
	@echo "------ installing dependencies ------"
	pip3 install -r requirements.txt

	@echo "\n------ migrating database ------"
	python3 migrations.py

	@echo "\n------ seeding database with 10,000,000 rows of data ------"
	# python3 seeder.py

	@echo "\n------ running server ------"
	screen -d -m uvicorn services.update:app --port 8001
	screen -d -m uvicorn services.read:app --port 8002

	@echo "\n------ cleaning up nginx ------"
	sudo rm /etc/nginx/sites-enabled/main.conf

	@echo "\n------ setting up nginx ------"
	sudo cp ./reverse-proxy/main.conf /etc/nginx/sites-available/main.conf
	sudo ln -s /etc/nginx/sites-available/main.conf /etc/nginx/sites-enabled/
	sudo /etc/init.d/nginx restart

clean:
	@echo "------ cleaning up ------"
	rm -rf ./reverse-proxy/main.conf
	rm -rf ./reverse-proxy/main.conf.bak

	# stop server
	screen -X -S update quit
	screen -X -S read quit

	@echo "\n------ done ------"
