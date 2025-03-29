from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def ingredientesView(request):
    return render(request, 'ingredientes.html')