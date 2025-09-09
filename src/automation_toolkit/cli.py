import logging
from typing import Optional
import typer

from .config import Settings
from .http import make_session

app = typer.Typer(help="Python automation toolkit CLI")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

@app.command()
def hello(name: str = typer.Option("world", "--name", "-n", help="Who to greet")):
    """Say hello."""
    typer.echo(f"Hello, {name}!")

@app.command("http:get")
def http_get(url: Optional[str] = typer.Argument(None),
             path: Optional[str] = typer.Option(None, help="Path to append to API base"),
             timeout: Optional[int] = typer.Option(None, help="Override HTTP timeout")):
    """GET a URL (or Settings.api_base_url + path)."""
    st = Settings()
    ses = make_session(timeout=timeout or st.http_timeout)
    target = url or (st.api_base_url.rstrip('/') + '/' + (path or ""))
    resp = ses.get_(target)
    typer.echo(resp.text)
