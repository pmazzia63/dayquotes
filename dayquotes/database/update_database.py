"""
Module to update the database with new quotes
"""
import json
from typing import TypedDict

from dayquotes.database.read_database import load_quotes


class Quote(TypedDict):
    id: int
    text: str
    author: str
    show: str
    comment: str


def update_quotes(quote_content: Quote):
    """
    Update the quotes database with a new quote

    :param quote_content: New quote to be added to the database
    :type quote_content: Quote
    """
    quotes = load_quotes()

    quotes["quotes"].append(quote_content)

    with open('quotes.json', 'w') as file:
        json.dump(quotes, file, indent=4)
