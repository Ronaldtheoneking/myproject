from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Articulo

def like(request, id, accion):
	#1.crear el objeto #2.editar objeto #3.guardar el objeto 
	#paso 1:
	art = Articulo.objects.get(pk=id)

	#paso 2:editar el objeto
	if accion == 'like':
		art.likes += 1
	else:
		art.dislike += 1

	#paso 3:guardar los cambios
	art.save()

	return HttpResponseRedirect(reverse('articulo', args=[art.slug]))
def articulo(request, slug):
	art = Articulo.objects.get(slug=slug)
	return render(request, 'articulo.html', {'articulo':art})

def index(request):
	# SELECT * FROM Articulos: queryset
	articulos = Articulo.objects.all().order_by('-id')



	return render(request, 'index.html', {'articulos':articulos})
