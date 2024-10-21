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

## Git practices
Other people are working on this project. **Do not ever push directly to `main`**. Always make a pull request either from your own branch or otherwise, and have others review and approve it. This is to ensure that we don't break the code base for everyone else.