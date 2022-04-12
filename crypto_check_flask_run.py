'''

python3 crypto_check_flask_run.py

'''

import os
from flask import Flask
from flask import send_file
from flask import render_template, request, redirect, url_for

import crypto_check
import pprint


app = Flask(__name__)


@app.route(
	'/query_transaction', 
	methods=['POST'])
def query_transaction():
	try:
		request_json = request.json
		result = crypto_check.query_by_transaction_id(
			request_json['transaction_id']
		)
		return result
	except:
		return None

'''
curl "http://localhost:9741/query_transaction" ^
--header "Content-Type: application/json" ^
--request POST ^
--data "{\"transaction_id\":\"da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ab\"}"

curl "http://localhost:9741/query_transaction" ^
--header "Content-Type: application/json" ^
--request POST ^
--data "{\"transaction_id\":\"da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ac\"}"
'''


@app.route(
	'/match_transaction', 
	methods=['POST'])
def match_transaction():
	try:
		request_json = request.json
		result = crypto_check.verify_transaction(
			transaction_id = request_json['transaction_id'],
			recevier_address = request_json['recevier_address'],
			transaction_amount = request_json['transaction_amount'],
			)
		return result
	except:
		return None

'''
curl "http://localhost:9741/match_transaction" ^
--header "Content-Type: application/json" ^
--request POST ^
--data "{\"transaction_id\":\"da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ab\",\"recevier_address\":\"TTJNvY9AfhRnWUDgAkUwaWr7SnqH1WTYyE\",\"transaction_amount\":159200000000}"


curl "http://localhost:9741/match_transaction" ^
--header "Content-Type: application/json" ^
--request POST ^
--data "{\"transaction_id\":\"da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ab\",\"recevier_address\":\"TTJNvY9AfhRnWUDgAkUwaWr7SnqH1WTYyD\",\"transaction_amount\":169200000000}"
'''


app.run(
	port = 9741,
	host = "0.0.0.0",
	debug = True,) 


'''
localhost:9741/check_transaction
'''