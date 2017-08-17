from django.db import models


class Filiale(models.Model):
    name = models.CharField('名称', max_length=32)
    leader = models.CharField('负责人', max_length=10)
    addr = models.CharField('地址', max_length=64)
    zipcode = models.IntegerField('邮编', null=True, default=0)
    phone = models.CharField('电话', max_length=16)
    fix = models.CharField('传真', max_length=16)
    Email = models.EmailField('邮箱')
    img = models.CharField(verbose_name='图片', max_length=255)
    weight = models.SmallIntegerField('权重')
    status = models.BooleanField('显示/关闭')

    class Meta:
        verbose_name_plural = '分支机构'

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField('名称', max_length=32)
    introduce = models.CharField('业务介绍', max_length=360)
    img = models.CharField(verbose_name='图片', max_length=255)
    weight = models.SmallIntegerField('权重', default=1)
    status = models.BooleanField('显示/关闭', default=0)

    class Meta:
        verbose_name_plural = '业务介绍'

    def __str__(self):
        return '%s-%s' % (self.weight, self.name)


class Consultation(models.Model):
    name = models.CharField('咨询人', max_length=32)
    phone = models.CharField('联系电话', max_length=11)
    project = models.CharField('项目名称', max_length=128)
    msg = models.TextField('咨询内容')
    status = models.BooleanField('审核状态', default=0)

    class Meta:
        verbose_name_plural = '咨询状态'

    def __str__(self):
        return '%s-%s' % (self.project, self.name)


class AboutModel(models.Model):
    about = models.TextField('关于我们')

    class Meta:
        verbose_name_plural = '关于我们'

    def __str__(self):
        return '关于我们内容页面'


class CaseModel(models.Model):
    # user = models.ForeignKey()
    title = models.CharField('标题', max_length=64)
    img = models.CharField('图片', max_length=255)
    content = models.TextField('内容')
    weight = models.SmallIntegerField('权重', default=1)
    status = models.BooleanField('显示/关闭', default=0)
    ctime = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '客户案例'

    def __str__(self):
        return self.title


class ZhaopinModel(models.Model):
    # user = models.ForeignKey()
    company = models.ForeignKey(Filiale, verbose_name='招聘公司')
    name = models.CharField('职位名称', max_length=64)

    xueli_choice = ((1, '博士'), (2, '研究生'), (3, '本科'), (4, '专科'),)
    xueli = models.SmallIntegerField('学历', choices=xueli_choice, default=3)

    age_s = models.CharField('年龄段', max_length=64, default='18-35')
    nub = models.SmallIntegerField('招聘人数', default=1)

    nature_choice = ((1, '全职'), (2, '兼职'), (3, '其他'),)
    nature = models.SmallIntegerField('工作性质', choices=nature_choice, default=1)

    qualifications = models.TextField('职位描述')
    requirement = models.TextField('任职要求')
    weight = models.SmallIntegerField('权重', default=1)
    status = models.BooleanField('显示/关闭', default=0)
    ctime = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '招聘信息'

    def __str__(self):
        return '%s-%s' % (self.company, self.name)
