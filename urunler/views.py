from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import models
from .models import Urun, Supplier
from .serializers import UrunSerializer, SupplierSerializer


class UrunListCreateView(generics.ListCreateAPIView):
    """
    Ürünleri listeleme ve yeni ürün ekleme endpoint'i
    GET: Tüm ürünleri listeler
    POST: Yeni ürün ekler
    """
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer

    def get(self, request, *args, **kwargs):
        """Tüm ürünleri listeler"""
        urunler = self.get_queryset()
        serializer = self.get_serializer(urunler, many=True)
        return Response({
            'success': True,
            'message': 'Ürünler başarıyla listelendi',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Yeni ürün ekler"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Ürün başarıyla eklendi',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Ürün eklenirken hata oluştu',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UrunRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Ürün detay, güncelleme ve silme endpoint'i
    GET: Ürün detayını getirir
    PUT: Ürünü tamamen günceller
    PATCH: Ürünü kısmen günceller
    DELETE: Ürünü siler
    """
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer

    def get(self, request, *args, **kwargs):
        """Ürün detayını getirir"""
        urun = self.get_object()
        serializer = self.get_serializer(urun)
        return Response({
            'success': True,
            'message': 'Ürün detayı başarıyla getirildi',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """Ürünü tamamen günceller"""
        urun = self.get_object()
        serializer = self.get_serializer(urun, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Ürün başarıyla güncellendi',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Ürün güncellenirken hata oluştu',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        """Ürünü kısmen günceller"""
        urun = self.get_object()
        serializer = self.get_serializer(urun, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Ürün başarıyla güncellendi',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Ürün güncellenirken hata oluştu',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """Ürünü siler"""
        urun = self.get_object()
        urun.delete()
        return Response({
            'success': True,
            'message': 'Ürün başarıyla silindi'
        }, status=status.HTTP_200_OK)


class SupplierListCreateView(generics.ListCreateAPIView):
    """
    Supplier'ları listeleme ve yeni supplier ekleme endpoint'i
    GET: Belirli bir ürünün supplier'larını listeler (product_id query parameter gereklidir)
    POST: Yeni supplier ekler
    """
    serializer_class = SupplierSerializer

    def get_queryset(self):
        queryset = Supplier.objects.all()
        product_id = self.request.query_params.get('product_id')
        if product_id:
            queryset = queryset.filter(urun_id=product_id)
        return queryset

    def get(self, request, *args, **kwargs):
        """Belirli bir ürünün supplier'larını listeler"""
        product_id = request.query_params.get('product_id')
        if not product_id:
            return Response({
                'success': False,
                'message': 'product_id query parameter is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        suppliers = self.get_queryset()
        serializer = self.get_serializer(suppliers, many=True)
        return Response({
            'success': True,
            'message': f'Suppliers for product {product_id} listed successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Yeni supplier ekler"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Supplier başarıyla eklendi',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Supplier eklenirken hata oluştu',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Supplier detay, güncelleme ve silme endpoint'i
    GET: Supplier detayını getirir
    PUT: Supplier'ı tamamen günceller
    PATCH: Supplier'ı kısmen günceller
    DELETE: Supplier'ı siler
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        """Supplier detayını getirir"""
        supplier = self.get_object()
        serializer = self.get_serializer(supplier)
        return Response({
            'success': True,
            'message': 'Supplier detayı başarıyla getirildi',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """Supplier'ı tamamen günceller"""
        supplier = self.get_object()
        serializer = self.get_serializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Supplier başarıyla güncellendi',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Supplier güncellenirken hata oluştu',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        """Supplier'ı kısmen günceller"""
        supplier = self.get_object()
        serializer = self.get_serializer(supplier, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Supplier başarıyla güncellendi',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Supplier güncellenirken hata oluştu',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """Supplier'ı siler"""
        supplier = self.get_object()
        supplier.delete()
        return Response({
            'success': True,
            'message': 'Supplier başarıyla silindi'
        }, status=status.HTTP_200_OK)


class ProductSupplierListView(generics.ListAPIView):
    """
    Belirli bir ürünün tedarikçilerini listeler
    GET: Ürüne ait tüm tedarikçileri listeler
    """
    serializer_class = SupplierSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Supplier.objects.filter(urun_id=product_id)

    def get(self, request, *args, **kwargs):
        """Belirli bir ürünün tedarikçilerini listeler"""
        product_id = self.kwargs['product_id']

        # Check if product exists
        try:
            product = Urun.objects.get(id=product_id)
        except Urun.DoesNotExist:
            return Response({
                'success': False,
                'message': f'Product with id {product_id} not found'
            }, status=status.HTTP_404_NOT_FOUND)

        suppliers = self.get_queryset()
        serializer = self.get_serializer(suppliers, many=True)
        return Response({
            'success': True,
            'message': f'Product {product_id} suppliers listed successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class UpdateStockView(generics.GenericAPIView):
    """
    Stok güncelleme endpoint'i
    POST: Belirtilen ürünün tedarikçi stoklarını günceller
    """

    def post(self, request, *args, **kwargs):
        print(request.data)
        """Ürün stoklarını günceller"""
        product_id = request.data.get('product_id')
        stock_updates = request.data.get('stock_updates', [])

        if not product_id:
            return Response({
                'success': False,
                'message': 'product_id is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not stock_updates:
            return Response({
                'success': False,
                'message': 'stock_updates is required and cannot be empty'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Urun.objects.get(id=product_id)
        except Urun.DoesNotExist:
            return Response({
                'success': False,
                'message': f'Product with id {product_id} not found'
            }, status=status.HTTP_404_NOT_FOUND)

        total_added = 0

        for update in stock_updates:
            supplier_id = update.get('supplier_id')
            quantity = update.get('quantity')

            if not supplier_id or quantity is None:
                return Response({
                    'success': False,
                    'message': 'Each stock_update must have supplier_id and quantity'
                }, status=status.HTTP_400_BAD_REQUEST)

            if quantity < 0:
                return Response({
                    'success': False,
                    'message': 'Quantity cannot be negative'
                }, status=status.HTTP_400_BAD_REQUEST)

            try:
                supplier = Supplier.objects.get(id=supplier_id, urun=product)
            except Supplier.DoesNotExist:
                return Response({
                    'success': False,
                    'message': f'Supplier with id {supplier_id} not found for this product'
                }, status=status.HTTP_404_NOT_FOUND)

            # Check if supplier has enough stock
            if quantity > supplier.miktar:
                return Response({
                    'success': False,
                    'message': f'Supplier {supplier.name} has only {supplier.miktar} items available, requested {quantity}'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Update supplier's quantity (subtract from available stock)
            supplier.miktar -= quantity
            supplier.save()
            total_added += quantity

        # Update product's total quantity by summing all suppliers' remaining quantities
        total_product_quantity = Supplier.objects.filter(urun=product).aggregate(
            total=models.Sum('miktar')
        )['total'] or 0

        product.miktar = total_product_quantity
        product.save()

        # Serialize the updated product
        serializer = UrunSerializer(product)

        return Response({
            'success': True,
            'message': f'Stock updated successfully. Added {total_added} items.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
