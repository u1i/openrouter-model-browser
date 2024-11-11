from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

API_ENDPOINT = "https://openrouter.ai/api/v1/models"

def fetch_model_data():
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return []

def human_readable_date(unix_timestamp):
    return datetime.datetime.fromtimestamp(unix_timestamp).strftime('%d %b %Y')

def sort_models(models, sort_by, order):
    reverse = order == 'desc'
    
    if sort_by == "name":
        key_func = lambda x: x['id'].split('/')[1] if '/' in x['id'] else x['id']
    elif sort_by == "date":
        key_func = lambda x: datetime.datetime.strptime(x['created'], '%d %b %Y')
    elif sort_by == "context_length":
        key_func = lambda x: x['context_length']
    else:
        key_func = lambda x: x['id'] # Default key

    return sorted(models, key=key_func, reverse=reverse)

@app.route('/', methods=['GET', 'POST'])
def model_browser():
    models = fetch_model_data()
    # Convert timestamps to human-readable format
    models = sorted(models, key=lambda x: x['created'], reverse=True) # Default sorting by date desc
    for model in models:
        model['created'] = human_readable_date(model['created'])
    
    sort_by = request.args.get('sort_by', default='date') # default to sort by date
    order = request.args.get('order', default='desc') # default to descending
    models = sort_models(models, sort_by, order)

    return render_template('model_browser.html', models=models)

if __name__ == '__main__':
    app.run(debug=True, port=8080)