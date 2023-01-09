from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Make an HTTP GET request to the API
    response = requests.get('https://api.coingecko.com/api/v3/coins/solana')
    # Parse the JSON response
    data = response.json()
    solana_price = data['market_data']['current_price']['usd']

    # Render the template and pass the Solana price to the template context
    return render_template('index.html', solana_price=solana_price)


if __name__ == '__main__':
    app.run(debug=True)
