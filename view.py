from django.shortcuts import render

#create your viewss here
def home(request):
	return render(request, "jobs_app/index.html")