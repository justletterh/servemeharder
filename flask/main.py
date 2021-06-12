#!/usr/bin/python3

# Trust Me, It's Faster This Way...
msg="""<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="icon" href="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png"/><title>Flask</title><style>:root{--x: 175px;}body{text-align: center; margin: 0;}div#flask a#flask img#flask{height: var(--x); width: var(--x);}div#flask a#bigflask img#bigflask{height: var(--x); width: auto;}div#flask a#flask img#flask, div#flask a#bigflask img#bigflask{display: inline-block;}div#flask{margin: 0; position: fixed; top: 50%; left: 50%; transform: translate(-50%,-50%); text-align: center;}</style></head><body><div id="flask"><a href="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png" id="flask"><img title="Flask's Icon." src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png" id="flask"></img></a><br/><a href="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" id="bigflask"><img id="bigflask" title="Flask's Large Icon." src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png"></img></a></div><script>document.addEventListener("DOMContentLoaded", ()=>{console.log("Hello From Flask!!!");});</script></body></html>"""
# LMAO

from flask import Flask
import sys
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = Flask(__name__)

@app.route('/')
def hello_world():
    return msg

def run():
    host="0.0.0.0"
    port="8018"
    app.run(host=host,port=port)

if __name__=="__main__":
    run()