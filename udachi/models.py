from django.db import models

# Create your models here.

class TipBluda(models.Model):
    class Meta:
        verbose_name = 'Тип блюда'
        verbose_name_plural = 'Типы блюда'


    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nazvanie


class Tara(models.Model):
    class Meta:
        verbose_name = 'Тара'
        verbose_name_plural = 'Тары'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    cena = models.FloatField('Цена', default=0 )

    def __str__(self):
        return self.nazvanie


class Bluda(models.Model):
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    opisanie = models.TextField('Описание', null=True, blank=True )
    cena = models.FloatField('Цена', default=0 )
    gramovka = models.FloatField('Граммовка', default=0 )
    prevyu = models.ImageField('Превью', null=False, blank=False )
    tip_bluda =  models.ForeignKey(TipBluda, verbose_name='Тип блюда' , on_delete=models.SET_NULL, null=True)
    tara_po_umolchaniu = models.ForeignKey(Tara, verbose_name='Тара по умолчанию' , on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nazvanie


class Ingridienti(models.Model):
    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nazvanie


class IngridientiVBlude(models.Model):
    class Meta:
        verbose_name = 'Ингридиент в блюде'
        verbose_name_plural = 'Ингридиенты в блюде'

    ingridient = models.ForeignKey(Ingridienti, verbose_name='Ингридиенты', on_delete=models.SET_NULL, null=True)
    bludo = models.ForeignKey(Bluda, verbose_name='Блюда', on_delete=models.SET_NULL, null=True)
    gramovka = models.FloatField('Граммовка',  )


class Akzia(models.Model):
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nazvanie


class Zakaz(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    sposob_otdachi = models.IntegerField(verbose_name='Способ отдачи', choices=(
        ('Самовывоз', 1),
        ('Доставка курьером', 2),
        ('На месте', 3),
    ))

    telephone = models.CharField(max_length=30, null=True, blank=True)
    fio = models.CharField('ФИО', max_length=255, null=True, blank=True)
    akzia = models.ForeignKey(Akzia, verbose_name='Акция', null=True, blank=True, on_delete=models.SET_NULL)
    data_i_vremia_zakaza = models.DateTimeField('Время заказа', auto_now_add=True, editable=False)
    adres = models.CharField('Адрес', max_length=255,  null=True, blank=True,)
    stolik = models.IntegerField('Номер столика',  null=True, blank=True,)


    def __str__(self):
        return f'#{self.id}'


class DetaliZakaza(models.Model):
    class Meta:
        verbose_name = 'Деталь заказа'
        verbose_name_plural = 'Детали заказа'

    zakaz = models.ForeignKey(Zakaz, verbose_name='Заказ', on_delete=models.CASCADE)
    bludo = models.ForeignKey(Bluda, verbose_name='Блюдо', null=True, blank=True, on_delete=models.SET_NULL)
    stoimost_na_moment_realizazii = models.FloatField('Цена на момент реализации', null=True, blank=True)
