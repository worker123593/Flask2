from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Поставь сто баллов'


@app.route('/<title>')
@app.route('/index/<title>')
def succes(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строит' in prof:
        title = 'Инженерные тренажеры'
    else:
        title = 'Научные симуляторы'
    return render_template('images.html', prof=prof, title=title)


@app.route('/list_prof/<list>')
def list_of_prof(list):
    list_prof = ['Пилот', 'Строитель', 'Врач', 'Астрогеолог', 'Экзобиолог', 'Штурман', ]
    return render_template('list_of_profession.html', type_list=list, list_prof=list_prof)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
