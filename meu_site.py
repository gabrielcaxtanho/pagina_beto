from flask import Flask, render_template, request, redirect




app = Flask(__name__)

app.secret_key = 'tiodino'


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/abrir_link')
def abrir_link():
    url = "https://encurtador.com.br/uFOU3"
    return redirect(url)

@app.route('/abrir_link2')
def abrir_link2():
    url = "https://wa.me/5541991010550"
    return redirect(url)



if __name__ == "__main__":
    app.run(debug=True)








