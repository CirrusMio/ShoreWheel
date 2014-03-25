from flask import Flask
app = Flask('ShoreWheel')

@app.route('/')
def index():
  return "Hello, World"


app.run()
