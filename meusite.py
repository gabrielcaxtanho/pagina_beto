from flask import Flask, render_template, request, redirect
from twilio.rest import Client



app = Flask(__name__)

app.secret_key = 'tiodino'


# Twilio credentials
account_sid = "AC5a91b8ed9c1596ad5e629395eecb7a72"
auth_token = "cc04b7051a92639106849aeb2df61237"

# Create a Twilio client
client = Client(account_sid, auth_token)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerta')
def alerta():
    message = client.messages.create(
                        to="+5561999076028",
                        from_="+13235181156",
                        body='Alerta do cachorro: BETO, Marcado como perdido')
    print(message.sid)
    return redirect('/')



@app.route('/pagina-mobile')
def pagina_mobile():
    return render_template('pagina_mobile.html')

@app.route('/abrir_link')
def abrir_link():
    url = "https://encurtador.com.br/uFOU3"
    return redirect(url)

@app.route('/abrir_link2')
def abrir_link2():
    url = "https://wa.me/5561999076028"
    return redirect(url)



if __name__ == "__main__":
    app.run(debug=True)
































