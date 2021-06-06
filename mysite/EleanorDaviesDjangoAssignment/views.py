from django.http import JsonResponse

# Create your views here.

def index(request):
    return JsonResponse(data = {

   Name  Oluwafemi Adenuga,

    Track  Backend(Python),

    Message  Hi, mentor, youre doing a great job

})
