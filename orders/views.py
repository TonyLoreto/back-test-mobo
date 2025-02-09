from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
from .models import Order
from .serializers import OrderSerializer
import openpyxl

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'])
    def uploadExcel(self, request):
        """Carga órdenes desde un archivo Excel y las guarda en la base de datos"""

        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            wb = openpyxl.load_workbook(file)
            sheet = wb.active
            orders_list = []

            for row in sheet.iter_rows(min_row=2, values_only=True):
                orderId, customerName, totalPrice, posId = row
                order_data = {
                    'orderId': orderId,
                    'customerName': customerName,
                    'totalPrice': totalPrice,
                    'posId': posId,
                    'status': 'completed'
                }
                serializer = OrderSerializer(data=order_data)
                if serializer.is_valid():
                    serializer.save()
                    orders_list.append(serializer.data)
                else:
                    return Response({'error': f'Invalid data in file: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Orders uploaded successfully', 'orders': orders_list}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

