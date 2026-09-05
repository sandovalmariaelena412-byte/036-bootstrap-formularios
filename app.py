from flask import Flask, render_template, request

app = Flask(__name__)

# Base de datos temporal en memoria, solo para practicar el login 
USUARIOS = {
    "admin": "1234",
    "elena": "html123"
}


# ---------- INICIO ----------
@app.route("/")
def inicio():
    return render_template("inicio.html")


# ---------- CLIENTES ----------
@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        nit = request.form.get("nit")
        correo = request.form.get("correo")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")

        return render_template(
            "clientes_confirmacion.html",
            nombre=nombre,
            nit=nit,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
        )

    # GET: solo muestra el formulario vacio
    return render_template("clientes.html")


# ---------- PROVEEDORES ----------
@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():
    if request.method == "POST":
        empresa = request.form.get("empresa")
        contacto = request.form.get("contacto")
        nit = request.form.get("nit")
        tipo_producto = request.form.get("tipo_producto")
        condicion_pago = request.form.get("condicion_pago")
        # El checkbox solo aparece en request.form si esta marcado
        activo = "Si" if request.form.get("activo") else "No"

        return render_template(
            "proveedores_confirmacion.html",
            empresa=empresa,
            contacto=contacto,
            nit=nit,
            tipo_producto=tipo_producto,
            condicion_pago=condicion_pago,
            activo=activo,
        )

    return render_template("proveedores.html")


# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        # Validacion simple contra el diccionario usuarios
        exito = usuario in USUARIOS and USUARIOS[usuario] == password

        return render_template(
            "login_resultado.html",
            exito=exito,
            usuario=usuario,
        )

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
