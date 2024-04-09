# FastAPI Playground

## Project Setup

Create a [python virtual environment](https://virtualenv.pypa.io/en/latest/installation.html)

```
virtualenv venv
source venv/bin/activate
```

Install dependancies

```
pip install -r requirements.txt
```

## Development

Start hot reload server

```
uvicorn api.main:app --reload --port 5000
```

## Project Structure
```
api/ - [fastapi app directory]
│
├── db/
│   │
│   └── db_models.py - [SQL Alchemy database model for postgres]
│
├── models/ - [pydantic models]
│   │
│   └── item.py
│
├── routers/ - [fastapi routers]
│   │
│   ├── root.py - [root router]
│   ├── items.py - [items router]
│   └── other_endpoints.py - [other endpoints router]   
│
├── main.py - [main fastapi server entrypoint]
│
└── utils.py - [fastapi utils]
```