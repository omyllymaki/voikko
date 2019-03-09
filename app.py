import json
import logging

from flask import Flask, request
from libvoikko import Voikko

app = Flask(__name__)
voikko = Voikko("fi")
logger = logging.Logger(__name__)


@app.route("/lemmatize", methods=['POST'])
def lemmatize():
    data = json.loads(request.data)
    tokens = data['tokens']

    result = {}
    for token in tokens:
        voikko_result = voikko.analyze(token)
        baseforms = [r['BASEFORM'].lower() for r in voikko_result]
        unique_baseforms = list(set(baseforms))
        result[token] = unique_baseforms

    return json.dumps(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
