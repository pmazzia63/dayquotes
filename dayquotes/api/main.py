import random

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dayquotes.api.utils import get_daily_seed
from dayquotes.database.read_database import load_quotes

app = FastAPI()


# Configurer le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet à toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes
    allow_headers=["*"],  # Permet tous les headers
)


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


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000
                )
