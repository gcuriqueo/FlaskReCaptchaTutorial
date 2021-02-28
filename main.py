from flask import *
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
app.config['RECAPTCHA_SITE_KEY'] = 'YOUR_RECAPTCHA_SITE_KEY'
app.config['RECAPTCHA_SECRET_KEY'] = 'YOUR_RECAPTCHA_SECRET_KEY'
recaptcha = ReCaptcha(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        if recaptcha.verify():
            message = 'Thanks for filling out the form!'
        else:
            message = 'Please fill out the ReCaptcha!'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
