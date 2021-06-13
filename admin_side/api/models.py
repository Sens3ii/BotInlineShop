from django.db import models
from jsonfield import JSONField


class TimedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimedBaseModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name="ID Пользователя Телеграм", unique=True, default=1)
    name = models.CharField(verbose_name="Имя пользователя", max_length=100)
    username = models.CharField(verbose_name="Username Телеграм", max_length=100, null=True)
    email = models.CharField(verbose_name="Email", max_length=100, null=True)

    def __str__(self):
        return f"№{self.id} ({self.user_id}) - {self.name}"


class Referral(TimedBaseModel):
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"

    id = models.ForeignKey(User, unique=True, primary_key=True, on_delete=models.CASCADE)
    referrer_id = models.BigIntegerField()

    def __str__(self):
        return f"№{self.id} - от {self.referrer_id}"


class Item(TimedBaseModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Название товара", max_length=50)
    photo = models.CharField(verbose_name="Фото file_id", max_length=200)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Описание", max_length=3000, null=True)

    def __str__(self):
        return f"№{self.id} - {self.name}"


class Purchase(TimedBaseModel):
    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.SET(0))
    item_id = models.ForeignKey(Item, verbose_name="Идентификатор Товара", on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name="Стоимость", decimal_places=2, max_digits=8)
    quantity = models.IntegerField(verbose_name="Количество")
    purchase_time = models.DateTimeField(verbose_name="Время покупки", auto_now_add=True)
    shipping_address = JSONField(verbose_name="Адрес Доставки", null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=100, null=True)
    receiver = models.CharField(verbose_name="Имя получателя", max_length=100, null=True)
    successful = models.BooleanField(verbose_name="Оплачено", default=False)

    def __str__(self):
        return f"№{self.id} - {self.item_id} ({self.quantity})"
