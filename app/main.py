import os
from urllib.parse import quote, urlparse
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="OldWeb.today / Netcapsule")
PYWB_BASE_URL = os.getenv("PYWB_BASE_URL", "http://localhost:8080").rstrip("/")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("app/static/index.html", "r", encoding="utf-8") as page:
        return page.read()

@app.get("/health")
def health():
    return {"status": "ok", "service": "netcapsule-web"}

@app.get("/go")
def go(url: str, timestamp: str = "20200101000000", browser: str = "firefox"):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return HTMLResponse("Informe uma URL http:// ou https:// válida.", status_code=400)
    allowed = {"mosaic", "netscape", "ie4", "ie5", "safari", "firefox", "chrome"}
    if browser not in allowed:
        browser = "firefox"
    digits = "".join(c for c in timestamp if c.isdigit())
    if len(digits) not in (4, 6, 8, 10, 12, 14):
        return HTMLResponse("Data inválida. Use ano, AAAAMMDD ou AAAAMMDDhhmmss.", status_code=400)
    digits = digits.ljust(14, "0")
    replay_url = f"{PYWB_BASE_URL}/archive/{digits}id_/{quote(url, safe=':/?&=%#@+;,$!()*[]')}"
    return RedirectResponse(replay_url, status_code=307)
