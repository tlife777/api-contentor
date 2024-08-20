from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from contentor.models import SensorData

# Create your views here.

@csrf_exempt
def register_data(request):
    if request.method=='POST':
        response = {}
        bateria = request.POST.get('bateria')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        volume = request.POST.get('volume')

        if bateria==None or latitude==None or longitude==None or volume==None:
            response = {"detail": "Required fields: bateria, latitude, longitude, volume"}
            return JsonResponse(response, status=400)
        
        try:
            result = SensorData.objects.create(
                bateria=bateria,
                latitude=latitude,
                longitude=longitude,
                volume=volume
            )
            if result:
                response = {
                    'id': result.id
                }
                return JsonResponse(response, status=201)
            else:
                return JsonResponse(response, status=500)
        except Exception as err:
            response = {
                "error": str(err)
            }
            return JsonResponse(response, status=500)

    response = {"detail": f"Method \"{request.method}\" not allowed."}
    return JsonResponse(response, status=405)
