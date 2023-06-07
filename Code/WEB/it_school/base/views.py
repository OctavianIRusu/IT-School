from django.views.generic import TemplateView

# Create your views here.

class LandingPage(TemplateView):
    
    template_name = "base/index.html"