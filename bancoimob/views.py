from django.http import JsonResponse
from .gameCore.gameRun import GameRun

def apiResponse(request):
    gameRun = GameRun()
    return JsonResponse(gameRun.run(), safe=False);
