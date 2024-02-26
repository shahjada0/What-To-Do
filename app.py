from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_random_activity():
    try:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = response.json()
        print(response.text)
        return data['activity']
    except Exception as e:
        return f"Error fetching activity: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_activity', methods=['POST'])
def get_activity():
    activity = get_random_activity()
    return activity

if __name__ == '__main__':
    app.run(debug=True)
