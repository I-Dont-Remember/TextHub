#! /usr/bin/env  python
import plivo,plivoxml
import sheets
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World from Flask"

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    print "in sms"
    from_num = request.values.get('From')
    to = request.values.get('To')
    text = request.values.get('Text')
    print "Message received - From: %s, To: %s, Text: %s" % (from_num, to, text)
    sheets.update(text)
    return 'Message received', 200

@app.route("/")
def main():
    return "Hello from main"

if __name__ == "__main__":
   # app.run(host='0.0.0.0', debug=True, port=80)
    app.run(port=1337)
