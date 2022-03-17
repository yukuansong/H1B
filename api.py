import flask
from flask import request, jsonify

import pandas as pd
import glob

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# input data (H1B, 2015 to 2019)

# read 2015
#df2015 = pd.read_csv('data/h2b2015.csv', dtype=str)
#df2016 = pd.read_csv('data/h2b2016.csv', dtype=str)
#df2017 = pd.read_csv('data/h2b2017.csv', dtype=str)
#df2018 = pd.read_csv('data/h2b2018.csv', dtype=str)
#df2019 = pd.read_csv('data/h2b2019.csv', dtype=str)
#df2020 = pd.read_csv('data/h2b2020.csv', dtype=str)
#df = pd.concat([df2015, df2016, df2017, df2018, df2019, df2020])
#fields = ['CASE_NUMBER', 'CASE_STATUS', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'FULL_TIME_POSITION', 'JOB_TITLE', 'NAIC_CODE', 'PW_UNIT_OF_PAY', 'WAGE_RATE_OF_PAY_FROM']
#df = pd.read_csv('FiveYear.csv', low_memory=False, dtype=str, skipinitialspace=True, usecols=fields)
#print(df.shape)

# read bank marketing data
df = pd.read_csv('data/bank-full.csv', dtype=str, skipinitialspace=True, header=0, delimiter=";")

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p> This site is a prototype API For distant reading of science fiction novels.</p>"


# A route to return a random row of H1B data frame
@app.route('/api/v1/resources/H1B/onecase', methods=['GET'])
def api_h1b():
    onecase = df.sample()
    onecase_json = dict()
    for col in onecase.columns:
        onecase_json[col] = onecase[col].values.tolist()

    return jsonify(onecase_json) 

app.run(host='0.0.0.0', port=5000)
