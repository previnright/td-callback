from flask import Flask, request, json, jsonify
import os
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
	if request.headers['Content-Type'] == 'application/json':
		my_info = json.dumps(request.json)
		enter_number = 14085836550 
		obj = json.loads(my_info)
		numb = obj["talkdesk_phone_number"]
		no_plus = numb.strip('+')
		to_int = int(no_plus)
		print("Talkdesk Phone Number Calling:", to_int)

		if to_int == enter_number:
			webbrowser.open('https://app.procedureflow.com')
			print("Number is equal, open Procedure Flow")

		else:
			print("Number is not equal, don't do anything")		

		return my_info

if __name__ == '__main__':
	app.run(debug=True)