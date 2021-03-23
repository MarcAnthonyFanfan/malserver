# Setting up Web Application Security Attack Infrastructure using Flask and Python with Juice Shop
The following guide assumes that you have Docker installed already, as installation methods on different operating systems can vary greatly.

## From-Scratch Setup
First we will walk through setting up the Docker container that will host our attack infrastructure.

1. Create a container running the latest version of Ubuntu 20.04.
You may use any linux distribution that you like, however the commands for installing the software we need might be different.
In this guide, we will be using the latest **Ubuntu 20.04 (Focal Fossa)**.
```
docker run -it -p 5000:5000 --name malserver ubuntu:focal
```

2. Within the container, install Python 3.
You should have automatically been presented an interactive shell.
The prompt should begin with **root@############** (#'s being random characters that make up your container's id).
```
apt update
apt install python3 python3-pip python3-venv -y
```

3. Within the container, create a folder for our project and a python virtual environment within that folder.
We will also be activating the python virtual environment (venv).
Any time you want to utilize the packages installed within your venv, you will need to activate it.
You can tell whether the venv has been activated, because afterwards the prompt should being with **(venv) root@############**.
Once the venv has been activated, we will install Flask.
```
mkdir malserver
cd malserver
python3 -m venv venv
. venv/bin/activate
pip3 install Flask
```