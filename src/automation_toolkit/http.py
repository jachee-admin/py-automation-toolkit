import time
import logging
from typing import Optional
import requests

log = logging.getLogger(__name__)

def make_session(retries: int = 3, backoff: float = 0.5, timeout: int = 15) -> requests.Session:
    s = requests.Session()

    def _request(method: str, url: str, **kwargs):
        last_exc: Optional[Exception] = None
        for attempt in range(1, retries + 1):
            try:
                resp = requests.request(method, url, timeout=timeout, **kwargs)
                resp.raise_for_status()
                return resp
            except Exception as e:  # noqa: BLE001
                last_exc = e
                log.warning("HTTP %s %s failed (attempt %s/%s): %s", method, url, attempt, retries, e)
                time.sleep(backoff * attempt)
        assert last_exc is not None
        raise last_exc

    # attach convenience methods
    s.get_ = lambda url, **kw: _request("GET", url, **kw)
    s.post_ = lambda url, **kw: _request("POST", url, **kw)
    s.put_ = lambda url, **kw: _request("PUT", url, **kw)
    s.delete_ = lambda url, **kw: _request("DELETE", url, **kw)
    return s
