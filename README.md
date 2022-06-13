# Experiment App to Apply Cache in Reverse Proxy

The code here also stored in a [github repository](https://github.com/AldiNFitrah/Nginx-Cache)

## How to Run
All the steps described below assumed that you're using UNIX base system.


### Requirements
- Python >=3.9
- Pip
- [Locust](https://locust.io/)
- [Screen](https://linuxize.com/post/how-to-use-linux-screen/) (optional)

### Steps
- run `make`
- If everything works fine, the app should now be discoverable on `http://localhost:8008`
- If not, then please do the following
  - Run the update service on port 8001
    ```python
    uvicorn services.update:app --port 8001
    ```
  - Run the read service on port 8002
    ```python
    uvicorn services.read:app --port 8002
    ```
  - Run Nginx
    ```bash
    sudo cp ./reverse-proxy/main.conf /etc/nginx/sites-available/main.conf

	sudo ln -s /etc/nginx/sites-available/main.conf /etc/nginx/sites-enabled/

	sudo /etc/init.d/nginx restart
    ```
  - Run the migration file
    ```python
    python3 migrations.py
    ```
  - (optional) Seed the database with a bunch of data (10 millions by default, might take a while)
    ```python
    python3 seeder.py
    ```
