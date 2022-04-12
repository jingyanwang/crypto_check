'''

python3 crypto_check_flask_run.py

'''

import os
from flask import Flask
from flask import send_file
from flask import render_template, request, redirect, url_for

import crypto_check
import pprint

result = crypto_check.query_by_transaction_id(
	'da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ab'
	)

pprint.pprint(result)

app = Flask(__name__)

app.run(
    port = 9741,
    host = "0.0.0.0",
    debug = True,) 


'''
localhost:9741
'''