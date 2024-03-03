from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# Home page that displays a message
@app.route('/')
def home():
    print(request.remote_addr)
    print(request.remote_user)
    print(request.headers)
    user_ip = request.remote_addr  # Assuming the client is not behind a proxy
    api_key = "d924f7b6ef1246309c09f73dd9ae0a43"
    response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={user_ip}")
    location_data = response.json()  # Convert the response to JSON
    print(location_data)
    return ""
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
