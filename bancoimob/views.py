from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from .gameCore.gameRun import GameRun

class API(GenericAPIView):
    def get(self, request):
        gameRun = GameRun()
        return JsonResponse(gameRun.run(), safe=False);
