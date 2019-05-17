from flask import Flask, request, json, jsonify
import os
import webbrowser
import requests

app = Flask(__name__)

@app.route('/')
def callback():
	talkdesk_phone_number = request.args.get('talkdesk_phone_number')
	contact_phone_number = request.args.get('contact_phone_number')
	talkdesk_phone_number = '+1' + talkdesk_phone_number
	contact_phone_number = '+1' + contact_phone_number
	url = 'https://talkforce.talkdeskid.com/oauth/token'
	body = 'scope=callback%3Awrite&grant_type=client_credentials'
	headers = {'Content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic YzQxODVhZjU2NzAyNDA5NzlkNGFmMjUwZmEwM2YwMDI6MlIzYTdmNldpS2xQckdqRUxYd2hjcmVpLW0wUlpFOEc5TFBFdThITHlNeFNheFRBNnQxYS1BVmJVMllwVFVUVzJNRTFCVzNDbXVUemh5OXFxaGEyQmc='}

	r = requests.post(url, data=body, headers=headers)
	json_data = json.loads(r.text)
	token = json_data['access_token']

	url2 = 'https://api.talkdeskapp.com/calls/callback'
	body2 = {}
	body2["talkdesk_phone_number"] = talkdesk_phone_number
	body2["contact_phone_number"] = contact_phone_number
	body2 = json.dumps(body2)
	print(body2)
	headers2 = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + token}

	r2 = requests.post(url2, data=body2, headers=headers2)
	print(r2)

	return '''<h1>Your talkdesk phone number is: {}<br>Your contact phone number is: {}</h1>'''.format(talkdesk_phone_number, contact_phone_number)

if __name__ == '__main__':
	app.run(debug=True)