from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from parser.serializers import TnvedSerializer
from parser.services.driver_manager import DriverChromeManager
from parser.services.tnved import get_tnved_code


@api_view(['GET'])
def tnved_view(request):

    key = request.query_params.get('key')
    if key is not None:
    
        with DriverChromeManager() as driver:
            
            data = get_tnved_code(product_name=key, driver=driver)
            
            if data:
                serializer = TnvedSerializer(data, many=True)
                return Response({"data": serializer.data})

    return Response("Произошла ошибка, повторите позже!", status=status.HTTP_400_BAD_REQUEST)