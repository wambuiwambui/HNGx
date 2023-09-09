from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime('%A')
    # Generate the current UTC time with the correct format
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Your GitHub repository URL and file URL
    github_repo_url = 'https://github.com/wambuiwambui/HNGx'
    github_file_url = 'https://github.com/wambuiwambui/HNGx/blob/master/app.py'
    
    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": datetime.datetime.now().strftime('%A'),
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url, 
        "status_code": 200
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


   