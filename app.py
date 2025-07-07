from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/wimbledon', methods=['GET'])
def get_wimbledon_result():
    year = request.args.get('year')
    if not year:
        return jsonify({'error': 'Year parameter is required'}), 400

    try:
        url = f"https://en.wikipedia.org/wiki/{year}_Wimbledon_Championships_–_Men%27s_singles"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape champion and runner-up
        infobox = soup.find('table', {'class': 'infobox'})
        rows = infobox.find_all('tr')

        champion, runner_up, score = '', '', ''
        for row in rows:
            header = row.find('th')
            data = row.find('td')
            if not header or not data:
                continue

            label = header.get_text(strip=True)
            value = data.get_text(strip=True)

            if 'Champion' in label:
                champion = value
            elif 'Runner-up' in label:
                runner_up = value
            elif 'Score' in label:
                score = value

        # Basic cleanup and check for tiebreak
        tiebreak = '(' in score
        sets = score.count(',') + 1

        return jsonify({
            'year': int(year),
            'champion': champion,
            'runner_up': runner_up,
            'score': score,
            'sets': sets,
            'tiebreak': tiebreak
        })

    except Exception as e:
        return jsonify({'error': 'Could not fetch data', 'details': str(e)}), 500


