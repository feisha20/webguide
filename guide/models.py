from django.db import models


# Create your models here.

# 栏目管理
class Titles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('title', max_length=200)  # 栏目名称
    is_main = models.BooleanField('is_main')  # 是否是主栏目
    sort = models.CharField('sort', max_length=200)  # 排序
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Titles管理'
        verbose_name_plural = 'Titles管理'

    def __str__(self):
        return self.Titles


# 网址管理
class Urls(models.Model):
    name = models.CharField('title_name', max_length=200)  # 网站名称
    url = models.CharField('name', max_length=200)  # 网址
    logo = models.ImageField(upload_to="logo")  # logo
    sort = models.CharField('logo_url', max_length=200)  # 排序
    update_time = models.DateTimeField('更新时间', auto_now_add=True)  # 更新时间，自动获取当前时间
    title = models.ForeignKey(Titles, to_field='id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Urls管理'
        verbose_name_plural = 'Urls管理'

    def __str__(self):
        return self.Urls
