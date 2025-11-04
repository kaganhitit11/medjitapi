from rest_framework import serializers
from .models import Urun, Supplier


class UrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urun
        fields = ['id', 'ad', 'miktar', 'fiyat', 'olusturma_tarihi', 'guncelleme_tarihi']
        read_only_fields = ['id', 'olusturma_tarihi', 'guncelleme_tarihi']


class SupplierSerializer(serializers.ModelSerializer):
    urun_detail = UrunSerializer(source='urun', read_only=True)
    urun = serializers.PrimaryKeyRelatedField(
        queryset=Urun.objects.all(),
        required=True
    )

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'quality', 'lead_time', 'urun', 'urun_detail', 'cost', 'olusturma_tarihi', 'guncelleme_tarihi']
        read_only_fields = ['id', 'olusturma_tarihi', 'guncelleme_tarihi', 'urun_detail']
