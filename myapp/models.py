from django.db import models

# Create your models here.


class Item(models.Model):
    '''
    品物の情報を格納するDBモデル
    '''
    name = models.CharField(max_length=100, null=False, verbose_name='品名')
    price = models.IntegerField(null=False, verbose_name='単価')
    quantity = models.IntegerField(null=False, verbose_name='数量')
    total = models.IntegerField(null=False, verbose_name='合計')
