from django.views.generic import ListView
from to_do.models import Todo

# Create your views here.

class MainPage(ListView):
    
    template_name = "to_do/index.html"
    model = Todo