from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Eleanor Davies Django Assessmentdata = {\n   Name  Eleanor Davies,\n    Track  Backend(Python),\n    Message  Hi mentor, thank you for teaching me. \n\n}")
