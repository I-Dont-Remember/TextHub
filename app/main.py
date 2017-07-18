#! /usr/bin/env  python
import plivo,plivoxml
import sheets
from flask import Flask,request
from collections import namedtuple
import ConfigParser
import config

# Depending on how this shapes up, a class for each person and their
#    number might be nice -- or dictionary

#class SMS(object):
#    from_num = ""
#    to_num = ""
#    text = ""
#
#    def __init__(self, from_num, to_num, text):
#        self.from_num = from_num
#        self.to_num = to_num
#        self.text = text

# Refresh/ Get Oauth token in the API file,
#   server gets called way wayyyy to infrequently
app = Flask(__name__)
@app.route("/hello")
def hello():
    return "Hello World from Flask"

# Find way to run multiple people on one phone number
@app.route("/sms", methods=['GET', 'POST'])
def message():
    from_num = request.values.get('From')
    to_num = request.values.get('To')
    text = request.values.get('Text')
    full_sms = sheets.SMS(from_num, to_num, text)
    print "Message received - From: %s, To: %s, Text: %s" % (from_num, to_num, text)
    sheets.handle_sms(full_sms)
    # Should we be returning something other than 200?
    return 'Message received', 200

@app.route("/")
def main():
    return "Uh-oh, I don't think you're supposed to be here."

if __name__ == "__main__":
     app.run(host='0.0.0.0', debug=True, port=80)
#    cp = ConfigParser.SafeConfigParser()
#    cp.read('sms.ini')
#    section = 'INFO'
#    PORT = cp.get(section, 'port')
#    SECRET = cp.get(section, 'client_file')
#    SHEET_NAME = cp.get(section, 'sheet_name')
#    print('sheet is "%s"' % SHEET_NAME)
#    print(SECRET)
#    PEOPLE = {}
#    if cp.has_section('PEOPLE'):
#        options = cp.options('PEOPLE')
#        for person in options:
#            PEOPLE[person] = cp.get('PEOPLE', person)
    # if confiig parsing fails, exit
#    app.run(port=config.port)
