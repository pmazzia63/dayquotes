import random

from fastapi import FastAPI

from dayquotes.api.utils import get_daily_seed
from dayquotes.database.read_database import load_quotes


app = FastAPI()


@app.get("/health/")
def read_root():
    return {"status": "ok"}


@app.get("/dayquote")
def read_day_quotes():
    quotes = load_quotes()
    dayli_seed = get_daily_seed()
    random.seed(dayli_seed)
    quote = random.choice(quotes["quotes"])

    return {"quote_content": quote}
