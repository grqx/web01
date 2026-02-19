from flask import Flask

app = Flask('app', static_folder='static', template_folder='templates')
