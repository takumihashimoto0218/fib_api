from flask import Flask
from api.routes import init_app

app = Flask(__name__)
init_app(app)

if __name__ == '__main__':
  app.run(debug=True)

