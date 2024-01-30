from flask import Flask, render_template, request
import requests

app = Flask(__name__)

class AstronomyInfo:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_astronomy_info(self, city, country, date=None):
        if date:
            api_url = f'https://api.ipgeolocation.io/astronomy?apiKey={self.api_key}&location={city},%20{country}&date={date}&lang=en'
        else:
            api_url = f'https://api.ipgeolocation.io/astronomy?apiKey={self.api_key}&location={city},%20{country}&lang=en'

        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/astronomy_info', methods=['POST'])
def astronomy_info():
    api_key = '8b9283e832064d979613c632e78a5248'
    astronomy_info = AstronomyInfo(api_key)
    
    country = request.form['country']
    city = request.form['city']
    date = request.form.get('date', None)
    astronomy_data=""
    if date:
        astronomy_data = astronomy_info.get_astronomy_info(city, country, date)
    else:
        astronomy_data = astronomy_info.get_astronomy_info(city, country)
    print(astronomy_data)
    if astronomy_data:
        return render_template('result.html',form_submitted=True,astronomy_data=astronomy_data)
    else:
        return "Error retrieving astronomy information."

if __name__ == '__main__':
    app.run(debug=True)
