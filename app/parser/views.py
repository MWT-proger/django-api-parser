from typing import List

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from parser.services.trts import get_trts_answer
from parser.services.tnved_to_okpd2 import convert_tnved_to_okpd2

from parser.serializers import DataOkpd2Serializer, DataTnvedSerializer, ErrorsSerializer, Okpd2Serializer, TnvedSerializer
from parser.services.driver_manager import DriverChromeManager
from parser.services.tnved import get_tnved_code

param = openapi.Parameter('key', openapi.IN_QUERY,
                          description="Ключ парсинга", type=openapi.TYPE_STRING)
success_response = openapi.Response('Список', DataTnvedSerializer)
okpd_success_response = openapi.Response('Okpd2', DataOkpd2Serializer)
errors_response = openapi.Response('Список', ErrorsSerializer)


@swagger_auto_schema(method='get', manual_parameters=[param], responses={200: success_response,400: errors_response})
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

@swagger_auto_schema(method='get', manual_parameters=[param], responses={200: okpd_success_response,400: errors_response})
@api_view(['GET'])
def tnved_okpd(request):

    key = request.query_params.get('key')
    if key is None:
        return Response({"errors": "Параметр key является обязательным."}, 
                        status=status.HTTP_400_BAD_REQUEST)

    with DriverChromeManager() as driver:

        
        data = convert_tnved_to_okpd2(tnved_code=key, driver=driver)

        if data:
            serializer = Okpd2Serializer(data)

            return Response({"data": serializer.data})
                

    return Response({"errors": "Информация не найдена."}, 
                    status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', manual_parameters=[param], responses={200: success_response,400: errors_response})
@api_view(['GET'])
def trts(request):

    key = request.query_params.get('key')
    if key is None:
        return Response({"errors": "Параметр key является обязательным."}, 
                        status=status.HTTP_400_BAD_REQUEST)

    with DriverChromeManager() as driver:

        
        data = get_trts_answer(product_name=key, driver=driver)

        if data:
            # serializer = TnvedSerializer(data, many=True)
            return Response({"data": data})

    return Response({"errors": "Информация не найдена."}, 
                    status=status.HTTP_400_BAD_REQUEST)
