import json
from typing import Dict


# Load quotes from JSON file
def load_quotes() -> Dict:
    """
    Read the JSON File and return the content of the file

    :return: Dict with the quotes
    :rtype: Dict
    """
    with open('dayquotes/database/database.json', 'r') as file:
        return json.load(file)
