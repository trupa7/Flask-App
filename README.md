# Flask-App
A basic “Hello World” API

## Features

• A basic “Hello World” API
• Functionality to enable logging
• Test coverage for your service


## Installation

Make sure you have install [python3](https://www.python.org/downloads/)

Check Python version
```bash
python --version
```

## Installing [pip](https://pip.pypa.io/en/stable/)
On macOS and Linux:
```bash
python3 -m pip install --user --upgrade pip
```
On Windows:
```bash
py -m pip install --upgrade pip
```


## Installing virtualenv
On macOS and Linux:
```bash
python3 -m pip install --user virtualenv
```
On Windows:
```bash
py -m pip install --user virtualenv
```

## Creating a virtual environment

On macOS and Linux:
```bash
python3 -m venv env
```
On Windows:
```bash
py -m venv env
```

## Activating a virtual environment

On macOS and Linux:
```bash
source env/bin/activate
```
On Windows:
```bash
.\env\Scripts\activate
```

## Install  requirements
• After activating python3 virtual please Install python packages
```bash
pip install requirements
```

## A command to start the application
run this code in virtual environment
```bash
python app.py
```

Open new cmd command terminal and test following cURL commands

get response without accept header
```bash
curl -i -X GET http://127.0.0.1:5000

get response with  accept header
```bash
curl -i -H "Accept: application/json" -X GET http://127.0.0.1:5000
```

get response with  accept header but not application/json
```bash
curl -i -H "Accept: application/javascript" -X GET http://127.0.0.1:5000
```

post response with out accept header
```bash
curl -i -X POST http://127.0.0.1:5000
```

post response with  accept header
```bash
curl -i -H "Accept: application/json" -X POST http://127.0.0.1:5000
```

get response with  accept header  but not application/json
```bash
curl -i -H "Accept: application/javascript" -X POST http://127.0.0.1:5000
```


stop running code first for unit tests
On macOS and Linux:
```bash
command + c
```
On Windows:
```bash
Clt+ c
```

A command to run the unit tests for your application
```bash
python unit_test.py
```
