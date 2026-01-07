from django.db import models


class Urun(models.Model):
    ad = models.CharField(max_length=200)
    miktar = models.PositiveIntegerField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-olusturma_tarihi']

    def __str__(self):
        return self.ad


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    quality = models.CharField(max_length=100)
    lead_time = models.PositiveIntegerField(help_text="Lead time in days")
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE, related_name='suppliers', help_text="Ürün bu tedarikçi tarafından teslim edilir")
    miktar = models.PositiveIntegerField(help_text="Amount this supplier can provide")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-olusturma_tarihi']

    def __str__(self):
        return self.name
