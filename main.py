from typing import Text
from flask import Flask, redirect, url_for, render_template
from flask.helpers import url_for
from datetime import datetime 

app = Flask(__name__)

# Context Processors - usar fechas actuales en las páginas
@app.context_processor
def date_now():
    return{ 
        'now' :datetime.utcnow()
    }
# Endpoints


@app.route('/') # vista genereal
def index():
    return 'Aprendiendo con Victor Robles y Pedro'


@app.route('/uso_plantilla') # vista con plantilla html
def plantilla():
    return render_template('index.html')


@app.route('/uso_plantilla_y_datos') # vista con plantilla html y envio de datos y listas
def plantilla_y_datos(): #http://127.0.0.1:5000/uso_plantilla_y_datos
    return render_template('plantilla_datos.html', 
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"]
                            )


@app.route('/uso_plantilla_condicionales_y_datos') # vista con plantilla html y envio de datos y listas
def plantilla_condicionales_y_datos(): #http://127.0.0.1:5000/uso_plantilla_condicionales_y_datos

    edad = 18

    return render_template('plantilla_datos_condicional.html', 
                            edad =edad, 
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"]
                            )


@app.route('/uso_for') # vista con plantilla html For y listas
def uso_for(): #http://127.0.0.1:5000/uso_for

    edad = 18
    personas =['Víctor', 'Paco', 'Francisco', 'David']

    return render_template('plantilla_datos_for.html', 
                            edad =edad, 
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"],
                            personas = personas
                            )

@app.route('/dividir_templates_con_include') # vista con plantilla html For y listas
def dividir_templates_con_include(): #http://127.0.0.1:5000/dividir_templates_con_include

    edad = 18
    personas =['Víctor', 'Paco', 'Francisco', 'David']

    return render_template('plantilla_includes.html', 
                            edad =edad, 
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"],
                            personas = personas
                            )




@app.route('/uso_plantilla_con_parametros')
@app.route('/uso_plantilla_con_parametros/<string:nombre>/<string:apellidos>') # vista con plantilla html y parametros que se pasan al html
def plantilla_parametros(nombre = None, apellidos = None):  #http://127.0.0.1:5000/uso_plantilla_con_parametros/Pedro/Gutierrez
    
    texto_defecto = ""

    if nombre != None and apellidos != None:
        
        texto_defecto =f"<h3>'envio desde main.py eres, {nombre} {apellidos}'</h3>"
        return render_template('plant_param.html', texto =texto_defecto)
    
    return f"""
        <h1>Página de información </h1>
        <p>Esta es la página de parametros</p>
         {texto_defecto} 
    """ 


@app.route('/menu') # vista con menu en plantilla
def menu():
    return render_template('index_menu.html')


    
@app.route('/informacion_menu') # vista informacion: Se pasa Parámetros
def informacion_menu():
    return f"""
        <h1>Página de información </h1>
        <p>Esta es la página de información</p>
        <h3>Bienvenido, </h3>
    """


@app.route('/informacion/<nombre>') # vista informacion: Se pasa Parámetros
def informacion(nombre):
    return f"""
        <h1>Página de información </h1>
        <p>Esta es la página de información</p>
        <h3>Bienvenido, {nombre}</h3>
    """

@app.route('/informacion2/<nombre>/<apellidos>') # vista informacion: Se pasa Varios Parámetros
def informacion2(nombre, apellidos):
    return f"""
        <h1>Página de información s</h1>
        <p>Esta es la página de información</p>
        <h3>Bienvenido, {nombre} {apellidos}</h3>
    """

@app.route('/informacion3/<string:nombre>/<string:apellidos>') # vista informacion: Se pasa Varios Parámetros obligando a ser string
def informacion3(nombre, apellidos):
    return """
        <h1>Página de información </h1>
        <p>Esta es la página de información</p>
        <h3>Bienvenido, {nombre} {apellidos} </h3> 
    """ .format()

@app.route('/informacion4/<string:Nombre>/<string:Apellidos>/<int:edad>') # vista informacion: Se pasa Varios Parámetros obligando a ser string o integer
def informacion4(Nombre, Apellidos, edad):
    return f"<h3>Bienvenido, {Nombre} {Apellidos} {edad}</h3>"

@app.route('/informacion5') # vista informacion: Parámetros Opcionales, 2 rutas para una misma función / Las dos funcionarán
@app.route('/informacion5/<string:Nombre>') 
@app.route('/informacion5/<string:Nombre>/<apellidos>') 
def informacion5(Nombre = None, apellidos = None):
    
    texto_defecto = ""

    if Nombre != None and apellidos != None:
        
        texto_defecto =f"<h3>Bienvenido, {Nombre} {apellidos}</h3>"

    
    return f"""
        <h1>Página de información </h1>
        <p>Esta es la página de información</p>
         {texto_defecto} 
    """ 


@app.route('/contacto') # REDIRECCION - vista contacto le ponemos otra segunda ruta por defecto para que tenga un parametro opcional
@app.route('/contacto/<redireccion>') # esto provoca redireccion http://127.0.0.1:5000/contacto/True a http://127.0.0.1:5000/lenguajes
def contacto(redireccion = None):

    if redireccion is not None :
        # si es diferente a none redireccione a otra ruta, la del lenguaje
        return redirect(url_for('lenguajes'))

    return "<h1>Página de Contacto</h1>"


@app.route('/lenguajes-disponibles') # vista Lenguajes
def lenguajes():
    return "<h1>Página de Lenguajes</h1>"


@app.route('/lenguajes-layout') # Renderizar template maestro
def lenguajes_layout():         # http://127.0.0.1:5000/lenguajes-layout
    return render_template('lenguajes_layout.html')


@app.route('/opcion_plantilla-Maestra2') # Renderizar template maestro
def otra_opcion_Plantilla_Maestra_layout():         # http://127.0.0.1:5000/opcion_plantilla-Maestra2
    return render_template('otra_opcion_Plantilla_Maestra.html')


@app.route('/opcion_plantilla-Maestra_hoja_estilos') # Renderizar template maestro con Hoja de Estilos
def otra_opcion_Plantilla_Maestra_layout_hoja_estilos():         # http://127.0.0.1:5000/opcion_plantilla-Maestra_hoja_estilos
    return render_template('layout_reutilizacion_hoja_estilos_opcion.html')



@app.route('/opcion_plantilla-Maestra_hoja_estilos2') # Renderizar template maestro con Hoja de Estilos2
def otra_opcion_Plantilla_Maestra_layout_hoja_estilos2():         # http://127.0.0.1:5000/opcion_plantilla-Maestra_hoja_estilos2
    return render_template('layout_reutilizacion_hoja_estilos2.html')




#@app.route('/<Help>') #vista envío parámetro
#def Help (Help):
#    return '<h1>The help {}! </h1>' .format(Help)


@app.route('/formulario') # vista formulario
def form():
    return """
        <html>
            <body>
                <h1>Data Processing</h1>
                </br>
                </br>
                <p> Insert your CSV file and then download the Result
          s      <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" class="btn btn-block"/>
                    </br>
                    </br>
                    <button type="submit" class="btn btn-primary btn-block btn-large">Pocess</button>
                </form>
            </body>
        </html>
    """    

if __name__ == '__main__': 
    app.run(debug=True)
    #reload auto