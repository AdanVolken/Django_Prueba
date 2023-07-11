from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Category, Article

# Create your views here.

layout = ("""

    <h1> Pagina web creada con Django</h1>
    <br><hr/><br>
    <ul>
        <li>
            <a href="{% url 'biblioteca' %}">Biblioteca </a> 
        </li>
        <li>
            <a href="{% url 'HolaMundo' %}">Hola Mundo </a> 
        </li>
         <li>
            <a href="{% url 'contacto' %}">Contacto </a> 
        </li>
    </ul>
    <hr/>
""")

def index(request):
    return render(request, 'index.html')


def hola_mundo(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto', nombre = "Adan", apellido = "Volken")

    return render(request, 'hola_mundo.html')



def biblioteca(request):

    html = ("""
        <h1> Hola soy la Paigina de Biblioteca </h1>
        <p> Lista de años que salieron libros:  </p>
        <ul>
    """)

    year = 2022
    while year <= 2050:

        if year %2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    return render(request, 'biblioteca.html')

def contacto(request, nombre = "", apellido = ""):

    
    html += f"<h2>{nombre}  {apellido}</h2>"


    return HttpResponse(layout + f"<h2> Hola como estas</h2>" + html )
    

def crear_articulo(request, title, content, public):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"<h1> Articulo creado: {articulo.title} - {articulo.content} </h1>")