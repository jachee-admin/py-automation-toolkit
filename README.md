# py-automation-toolkit

Minimal but robust Python automation toolkit with a clean CLI, config management, HTTP utilities with retries, and tests.

## Features
- Typer CLI with subcommands (`hello`, `http:get`).
- Pydantic-based settings management via environment variables and `.env` support.
- Requests session with retries + backoff.
- Structured logging.
- pytest example.

## Quickstart
```bash
uv venv || python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytool --help
pytool hello --name username
pytool http:get https://httpbin.org/get
pytest -q
```
