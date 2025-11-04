from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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
    GET: Tüm supplier'ları listeler
    POST: Yeni supplier ekler
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        """Tüm supplier'ları listeler"""
        suppliers = self.get_queryset()
        serializer = self.get_serializer(suppliers, many=True)
        return Response({
            'success': True,
            'message': 'Supplier\'lar başarıyla listelendi',
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
