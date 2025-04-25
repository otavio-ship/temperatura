from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def converter_temperatura():
    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])

            # Conversões
            fahrenheit = (celsius * 9 / 5) + 32
            kelvin = celsius + 273.15

            return render_template('conversor.html',
                                   celsius=celsius,
                                   fahrenheit=round(fahrenheit, 2),
                                   kelvin=round(kelvin, 2))

        except ValueError:
            return render_template('conversor.html', erro="Por favor, digite uma temperatura válida!")

    return render_template('conversor.html')


if __name__ == '__main__':
    app.run(debug=True)