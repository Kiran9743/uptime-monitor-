import httpx
import threading
import time
from datetime import datetime

# Very small in-memory store for demo purposes
_monitor_status = {}

DEFAULT_INTERVAL = 60  # seconds

def _check_url(name, url):
    try:
        r = httpx.get(url, timeout=10.0)
        status = "up" if r.status_code < 400 else "down"
    except Exception:
        status = "down"
    _monitor_status[name] = {"url": url, "status": status, "last_checked": datetime.utcnow().isoformat()}

def _monitor_loop():
    # example monitors
    monitors = [
        ("Example", "https://example.com"),
    ]
    while True:
        for name, url in monitors:
            _check_url(name, url)
        time.sleep(DEFAULT_INTERVAL)

_monitor_thread = None

def start_monitoring():
    global _monitor_thread
    if _monitor_thread is None:
        _monitor_thread = threading.Thread(target=_monitor_loop, daemon=True)
        _monitor_thread.start()

def get_status():
    return _monitor_status
