from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = ("""

    <h1> Pagina web creada con Django</h1>
    <br><hr/><br>
    <ul>
        <li>
            <a href="/biblioteca">Biblioteca </a> 
        </li>
        <li>
            <a href="/hola_mundo">Hola Mundo </a> 
        </li>
         <li>
            <a href="/contacto">Contacto </a> 
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

    html = ""

    if nombre and apellido:
            html = f"<h2>{nombre}  {apellido}</h2>"


    return HttpResponse (layout + f"<h2> Hola como estas  {html}  mi numero es 342323 </h2>")
    
