# cosc471droneproject

## Getting Started
### Clone the repository and CD into the directory
```bash
git clone https://github.com/joshrandall8478/cosc471droneproject.git
cd cosc471droneproject
```
You can optionally use `gh` to clone the repository as well:
```bash
gh repo clone joshrandall8478/cosc471droneproject
cd cosc471droneproject
```
### Set up the virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

> `.venv` is in `.gitignore`. Please try to use `.venv` for the virtual environment name. Do **NOT** commit the virtual environment to the repository.

At this point you should be good to go. You can run the program while sourced inside of the virtual environment. To exit the virtual environment, simply type `deactivate`. Make sure your IDE is set up to use the virtual environment as well. Visual Studio Code should automatically detect the virtual environment and use it.

## Starting MySQL in Docker
It is not required to use mySQL in Docker. If you are running mySQL baremetal, you can use that.
> The credentials regardless should be user: "droneuser" and password: "dronepassword" (for development purposes only).
To start the mySQL container within the docker compose file, make sure your working directory is the root of the project and run the following command:
```bash
docker compose up -d
```
`-d` daemonizes the container so that it runs in the background. To stop the container, run the following command:
```bash
docker compose down
```
To enter the mySQL container, run the following command:
```bash
docker compose exec -it db mysql -u droneuser -p
```
You will be prompted for the password. Enter `dronepassword` and you should be in the mySQL shell.

## Running the PHP site
Make sure you have php installed, and mySQL with the drone database and dronestats table initialized. If you don't have those databases created, the python program should automatically create them for you. 

You can run a php server either by using an extension (this [VS code extension](https://marketplace.visualstudio.com/items?itemName=brapifra.phpserver) works the best), or by run the following command:
```bash
php -S localhost:8000
```

## Git practices
Other people are working on this project. **Do not ever push directly to `main`**. Always make a pull request either from your own branch or otherwise, and have others review and approve it. This is to ensure that we don't break the code base for everyone else.