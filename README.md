#  Wimbledon Final Result API

A simple Flask API that scrapes Wikipedia to return Men's Singles Wimbledon final results by year.

##  Features

- Scrapes champion, runner-up, final score, set count, and tiebreak presence
- Pulls live data directly from Wikipedia
- Returns JSON response on GET requests

---

##  How to Run Locally

 1. Clone the repository

```bash
git clone https://github.com/yourusername/wimbledon-api.git
cd wimbledon-api

2. Install dependencies

 pip install -r requirements.txt

3. Run the Flask server

python app.py


 Example API Request

 http://localhost:5000/wimbledon?year=2022
 
 Response:

 {
  "year": 2022,
  "champion": "Novak Djokovic",
  "runner_up": "Nick Kyrgios",
  "score": "4–6, 6–3, 6–4, 7–6(7–3)",
  "sets": 4,
  "tiebreak": true
}
