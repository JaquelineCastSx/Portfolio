from flask import Flask, redirect, url_for, render_template
import math as mt
from datetime import datetime
app = Flask(__name__)

#Context processor
@app.context_processor
def fecha():
    return{
        'date' : datetime.utcnow()
    }

@app.route('/')
def index():
    ##Instrucciones de back-end
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():

    return render_template('proyectos.html')
    

@app.route('/contacto')
def contacto():
    
    return render_template("contacto.html")

@app.route('/plantillas')    
def plantillas():
    #Variable que se despliega en for
    skills = [
        "HTML5",
        "CSS",
        "Bootstrap",
        "JavaScript",
        "Adobe Illustrator",
        "Adobe Photoshop",
        "Figma",
        "Angular"
    ]

    return render_template("plantilla.html", skills=skills)

#Manejador de errores
@app.errorhandler(404)
def page_not_found(e):
    error_message = "The page you're looking for doesn't exist."

    return render_template('error.html', error_message=error_message), 404


if __name__ == '__main__':
    app.run(host = '0.0.0.0')