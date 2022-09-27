
from django.http import HttpResponse, HttpRequest  # JsonResponse


def main(request: HttpRequest):  # -> JsonResponse:
    return HttpResponse('Hello from "ADA Collection"!')
    # return JsonResponse(data={
    #     'error': False,
    #     'status': 'Hello from "ADA Collection"!',
    #     'details': None
    # }, status=200)
