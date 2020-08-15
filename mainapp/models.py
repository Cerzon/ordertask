""" Order models
"""
from django.db import models


class OrderHeader(models.Model):
    """ Order header - registration Id and creation date
    """
    reg_id = models.CharField(
        verbose_name='регистрационный номер заказа',
        max_length=11
    )
    created = models.DateTimeField(
        verbose_name='дата и время создания',
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ №{self.reg_id}'


class OrderItem(models.Model):
    """ Order item - price, amount, good Id and stuff
    """
    order = models.ForeignKey(
        OrderHeader,
        on_delete=models.CASCADE,
        related_name='item'
    )
    vendor_code = models.CharField(
        verbose_name='артикул',
        max_length=8
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2
    )
    amount = models.DecimalField(
        verbose_name='количество товара',
        max_digits=5,
        decimal_places=2
    )

    class Meta:
        ordering = ('order',)
        verbose_name = 'товар в заказе'
        verbose_name_plural = 'товары в заказе'

    def __str__(self):
        return f'{self.order} - {self.vendor_code} - p = {self.price}, q = {self.amount}'
