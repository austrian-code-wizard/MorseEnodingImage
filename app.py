from flask import Flask, render_template, flash, send_from_directory
from flask_bootstrap import Bootstrap
from config import Config
from form import InputForm
from pattern_generator import plot_dvd
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        flash("Encoding...")
        path = plot_dvd(f"result{random.randint(0, 1000000)}.svg", form.length.data, form.height.data, form.text.data, form.bit_length.data, form.stroke.data, form.spacing.data)
        result = open(path).read()
        return render_template('result.html', result=result, download_path=path)
    return render_template('index.html', title='Encode', form=form)


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(".", filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
