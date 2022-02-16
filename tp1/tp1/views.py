from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context




def holamundo(request):
    doc_externo = open("C:/Users/Alejandro/Documents/Python/django/tp1/tp1/templates/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close() 
    documento = plt.render

    ctx = Context({"lineas":range(10)})
    documento =  plt.render(ctx)
    return HttpResponse(documento)
    #return HttpResponse("Hola mundo. Django")

