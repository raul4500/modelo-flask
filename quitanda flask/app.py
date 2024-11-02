from flask import*
from controller import *


app = Flask(__name__)
app.register_blueprint(produto_bp)

if __name__ == '__main__':
    app.run(debug=True)
