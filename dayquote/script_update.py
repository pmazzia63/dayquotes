import json
import os

import numpy as np

if __name__ == "__main__":
    # Load the quotes from  the json file from current directory
    path_json = os.path.dirname(os.path.abspath(__file__)) + "/data_base.json"

    with open(path_json, 'r') as file:
        quotes = json.load(file)

    list_quotes = quotes["quotes"]

    # Generer un nombre aléatoire pour choisir une citation
    nb_quote = np.random.randint(0, len(list_quotes))

    quote = list_quotes[nb_quote]["quote"]
    author = list_quotes[nb_quote]["author"]

    html_code = f"""
        <!DOCTYPE html>
    <html>
    <head>
        <title>Citation Inspirante</title>
        <style>
            body{{
                font-family: Arial, sans-serif;
                color: black;
                background-color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .citation-container {{
                text-align: center;
            }}
            .citation {{
                font-size: 24px;
            }}
            .auteur {{
                margin-top: 20px;
                font-size: 20px;
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        <div class="citation-container">
            <div class="citation">"{quote}"</div>
            <div class="auteur">{author}</div>
        </div>
    </body>
    </html>
        """

    # Save the html code in a file
    path_html = os.path.dirname(os.path.abspath(__file__)) + "/index.html"

    with open(path_html, 'w') as file:
        file.write(html_code)
