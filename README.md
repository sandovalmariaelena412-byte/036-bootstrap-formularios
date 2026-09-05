# 036-bootstrap-formularios

Proyecto Flask + Bootstrap para la tarea "Formularios de Negocio con Bootstrap y Flask"

## Cómo ejecutar el proyecto

1. pip install flask
  
2. cd 036-bootstrap-formularios

3. Ejecuta la aplicación:
 
   python app.py

4. Abrir el navegador en:
 
   http://localhost:5000
   

## Estructura del proyecto


036-bootstrap-formularios/
  app.py
  templates/
    base.html
    inicio.html
    clientes.html
    clientes_confirmacion.html
    proveedores.html
    proveedores_confirmacion.html
    login.html
    login_resultado.html
  static/
    estilos.css


## Notas importantes

- Los datos de los formularios **no se guardan de forma permanente** (no hay base de datos ni archivos). Cada formulario recibe la información por POST y la muestra en pantalla como confirmación.
- El login usa un diccionario `USUARIOS` definido directamente en `app.py`, sin cifrado. Es solo para practicar rutas, formularios y condicionales.
- Usuario de prueba: `admin` / Contraseña: `1234`

## Componente extra (bonus)

Se agregó un **tooltip de Bootstrap** (`data-bs-toggle="tooltip"`) junto al campo de contraseña en la página de login, que muestra el usuario y contraseña de prueba al pasar el mouse sobre el ícono de información. Se activa con el JavaScript de Bootstrap (`bootstrap.Tooltip`) incluido al final de `login.html`.
