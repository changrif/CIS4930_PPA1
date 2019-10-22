import flask
from flask import request, jsonify
import logging
import sys

from main import bmi, email, db

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = flask.Flask(__name__)

app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/bmi', methods=['GET'])
def api_bmi():
    if 'feet' in request.args and 'inches' in request.args and 'weight' in request.args:
        try:
            category, bmiNum = bmi.calculate(request.args['feet'], request.args['inches'], request.args['weight'])

            return jsonify(db.saveBMI(request.args['feet'], request.args['inches'], request.args['weight'], category, bmiNum))
        except:
            pass
    elif not request.args:
        return jsonify(db.getBMI())
    return flask.jsonify(error=400, text=str("Bad Request: The requested URL requires either no parameters (to view all bmi requests in the databse) or the arguments 'feet', 'inches' and 'weight' as integers.")), 400

@app.route('/email', methods=['GET'])
def api_email():
    if 'address' in request.args:
        try:
            verified = email.verify(request.args['address'])
            
            return jsonify(db.saveEmail(verified, request.args['address']))
        except:
            pass
    elif not request.args:
        return jsonify(db.getEmails())
    return flask.jsonify(error=400, text=str("Bad Request: The requested URL requires either no parameters (to view all email requests in the database) or the argument 'email' as a string.")), 400

@app.errorhandler(404)
def page_not_found(e):
    return flask.jsonify(error=404, text=str(e)), 404
        
def run():
    app.run()