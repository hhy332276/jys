from flask import Blueprint,render_template,current_app

main = Blueprint('main', __name__)
@main.route('/index/')
def index():
    current_app.logger.info('fdfdfd')
    return render_template('main/index.html')