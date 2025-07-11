# Production-Ready-RAG-Application

The main target of this project is model for question answering

## Requirements

-Python 3.12.9

#### Install Python Using MiniConda
1-Download and install from [here](https://www.anaconda.com/docs/main)

2- create a new environment from the following command:
```bash
conda create -n myenv python==3.12.9
```
3- Activate the environment:
``` bash
conda activate myenv
```
## Installation
### Install the packages
``` bash
pip install -r requirements.txt
```

#### Setup the environment variables
If You are  Using CMD using this command
``` 
copy .env.example .env
```
If You are  Using WSL using this command
``` 
cp .env.example .env
```
and you can create file manually called .env and copy values from .env.example to .env

Set your environment in the '.env' file .like 'OPENAI_API_KEY' .
