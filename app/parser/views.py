from typing import List

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from parser.serializers import DataTnvedSerializer, TnvedSerializer
from parser.services.driver_manager import DriverChromeManager
from parser.services.tnved import get_tnved_code

param = openapi.Parameter('key', openapi.IN_QUERY,
                          description="Ключ парсинга", type=openapi.TYPE_STRING)
success_response = openapi.Response('Список', DataTnvedSerializer)


@swagger_auto_schema(method='get', manual_parameters=[param],
                     responses={200: success_response, 
                                400: {"errors": "Информация об ошибках"}})
@api_view(['GET'])
def tnved_view(request):

    key = request.query_params.get('key')
    if key is None:
        return Response({"errors": "Параметр key является обязательным."}, 
                        status=status.HTTP_400_BAD_REQUEST)

    with DriverChromeManager() as driver:

        data = get_tnved_code(product_name=key, driver=driver)

        if data:
            serializer = TnvedSerializer(data, many=True)
            return Response({"data": serializer.data})

    return Response({"errors": "Информация не найдена."}, 
                    status=status.HTTP_400_BAD_REQUEST)
