#! /usr/bin/env  python
import plivo,plivoxml
import sheets
from flask import Flask, send_file, request
from collections import namedtuple

# Depending on how this shapes up, a class for each person and their
#    number might be nice

class SMS(object):
    from_num = ""
    to_num = ""
    text = ""

    def __init__(self, from_num, to_num, text):
        self.from_num = from_num
        self.to_num = to_num
        self.text = text

# Refresh/ Get Oauth token in the API file, 
#   server gets called way wayyyy to infrequently
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World from Flask"

# Find way to run multiple people on one phone number
@app.route("/sms", methods=['GET', 'POST'])
def sms():
    print "in sms"
    from_num = request.values.get('From')
    to_num = request.values.get('To')
    text = request.values.get('Text')
    full_sms = SMS(from_num, to_num, text)
    print "Message received - From: %s, To: %s, Text: %s" % (from_num, to_num, text)
    sheets.update(full_sms)
    return 'Message received', 200

@app.route("/")
def main():
    return "You're at Home"

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True, port=80)
    app.run(port=1337)
