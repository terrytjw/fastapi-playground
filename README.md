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
uvicorn src.main:app --reload --port 5000
```

## Project Structure

- `src/main.py` main fastapi server entrypoint
- `src/db/model.py` SQL Alchemy database model for postgres