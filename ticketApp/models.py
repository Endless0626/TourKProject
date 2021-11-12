from django.db import models
import django.utils.timezone as timezone
class Ticket(models.Model):
    TICKET_CHOICES = (
        ('中国-韩国', '中国-韩国'),
        ('韩国-中国', '韩国-中国'),
    )
    AIRPORTLINES_CHOICES = (
        ('大韩航空', '大韩航空'), ('韩亚航空', '韩亚航空'), ('山东航空', '山东航空'),
        ('青岛航空', '青岛航空'), ('春秋航空', '春秋航空'), ('釜山航空', '釜山航空'),
        ('中国南方航空', '中国南方航空'), ('真航空', '韩亚航空'), ('中国国际航空', '中国国际航空'),
        ('中国东方航空', '中国东方航空'), ('济州航空', '济州航空'),
    )
    SIZE_CHOICES = (
        ('大型机', '大型机'),
        ('中型机', '中型机'),
        ('小型机', '小型机'),
    )
    CHANGE_CHOICES = (
        ('可退改签', '可退改签'),
        ('不可退改签', '不可退改签'),
    )
    FOOD_CHOICES = (
        ('有餐食', '有餐食'),
        ('不提供餐食', '不提供餐食'),
    )
    SITE_CHOICES = (
        ('经济舱', '经济舱'),
        ('商务舱', '商务舱'),
        ('头等舱', '头等舱'),
    )
    ticketType = models.CharField(choices=TICKET_CHOICES, max_length=10, verbose_name='飞机航向')
    airportType = models.CharField(choices=AIRPORTLINES_CHOICES, max_length=10, verbose_name='航空公司')
    logo = models.ImageField(upload_to='Airport/', blank=True, verbose_name="航空公司标志")
    number = models.CharField(max_length=10, verbose_name="航班号")
    sizeType = models.CharField(choices=SIZE_CHOICES, max_length=20, verbose_name='机体类型')
    off = models.CharField(max_length=50, verbose_name="起飞城市")
    offAirport = models.CharField(max_length=50, verbose_name="起飞机场")
    offTime = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='起飞时间')
    middlePlace = models.CharField(max_length=10, blank=True, null=True, verbose_name="中转城市")
    middleTime = models.CharField(max_length=20, blank=True, null=True, verbose_name="中转时间")
    land = models.CharField(max_length=50, verbose_name="降落城市")
    landAirport = models.CharField(max_length=50, verbose_name="降落机场")
    landTime = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='降落时间')
    flyTime = models.CharField(max_length=50, verbose_name="飞行时间")
    siteType = models.CharField(choices=SITE_CHOICES, max_length=5, verbose_name='座位等级')
    changeType = models.CharField(choices=CHANGE_CHOICES, max_length=10, verbose_name='退改签')
    foodType = models.CharField(choices=FOOD_CHOICES, max_length=10, verbose_name='餐食提供')
    luggageWeight = models.CharField(max_length=30, verbose_name="行李额")
    price = models.IntegerField(blank=True, null=True, verbose_name='机票价格')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = '航班'
        verbose_name_plural = '航班'
        ordering = ('-offTime', )

class selfService(models.Model):
    AIRPORTLINES_CHOICES = (
        ('大韩航空', '大韩航空'), ('韩亚航空', '韩亚航空'), ('山东航空', '山东航空'),
        ('青岛航空', '青岛航空'), ('春秋航空', '春秋航空'), ('釜山航空', '釜山航空'),
        ('中国南方航空', '中国南方航空'), ('真航空', '真航空'), ('中国国际航空', '中国国际航空'),
        ('中国东方航空', '中国东方航空'), ('济州航空', '济州航空'),
    )
    Name = models.CharField(choices=AIRPORTLINES_CHOICES, max_length=10, verbose_name='航空公司')
    Code = models.CharField(max_length=5, blank=True, null=True, verbose_name='航空公司代号')
    Time = models.CharField(max_length=50, blank=True, null=True, verbose_name='自助值机时间')
    Home = models.CharField(max_length=100, blank=True, null=True, verbose_name='航空公司官网')
    Logo = models.ImageField(upload_to='Airport/', blank=True, verbose_name="航空公司标志")

    class Meta:
        verbose_name = '航空公司信息'
        verbose_name_plural = '航空公司信息'

