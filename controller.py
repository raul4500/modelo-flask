from flask import*
from model import*

app_controller = Blueprint('controller', __name__)

@app_controller.route('/')
def main():
    return render_template('index.html', mensagem=mensagem)