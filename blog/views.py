from django.shortcuts import render

#from django.views import generic
# Create your views here.


def Index(request):
	return render(request, 'blog/index.html')
		
