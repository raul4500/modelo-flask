from flask import *
from database import init_db
from controllers.controller import*

app = Flask(__name__)
app.register_blueprint(app_controller)

if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)
