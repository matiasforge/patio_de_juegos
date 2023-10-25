from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('cajas.html', cajas=3)

@app.route('/play/<int:cajas>')
def play_cajas(cajas):
    return render_template('cajas.html', cajas=cajas)

@app.route('/play/<int:cajas>/<color>')
def play_cajas_color(cajas, color):
    return render_template('cajas.html', cajas=cajas, color=color)

if __name__ == '__main__':
    app.run(debug=True)
