from azure.identity import InteractiveBrowserCredential
from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = 'mysecretkey'

credential = InteractiveBrowserCredential()

@app.route('/login')
def login():
    # Obtener la URL de inicio de sesión de Azure AD
    auth_url = credential.get_authorization_request_url(scopes=['openid', 'profile'])

    # Almacenar el estado de autenticación en la sesión
    session['auth_state'] = credential.auth_state

    # Redirigir al usuario a la página de inicio de sesión de Azure AD
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Obtener el estado de autenticación almacenado en la sesión
    auth_state = session.pop('auth_state', None)

    # Procesar la respuesta de la página de inicio de sesión de Azure AD
    credential.get_token_from_authorization_code(request.url, auth_state=auth_state)

    # Redirigir al usuario a la página principal de la aplicación web
    return redirect('/')
