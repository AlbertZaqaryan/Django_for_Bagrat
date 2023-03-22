from django.db import models

# Create your models here.

class SiteName(models.Model):

    name = models.CharField('Site name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SiteName'
        verbose_name_plural = 'SiteNames'


class HomeBg(models.Model):

    name = models.CharField('HomeBg name', max_length=60)
    text = models.TextField('HomeBg text')
    img = models.ImageField('HomeBg image', upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'HomeBg'
        verbose_name_plural = 'HomeBgs'


class Info(models.Model):

    name = models.CharField('Info name', max_length=30)
    img = models.ImageField('Info image', upload_to='images')
    text1 = models.TextField('Info text1')
    text2 = models.TextField('Info text2')


    def __str__(self):
        return self.name
    
        
    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'


class Product(models.Model):

    name = models.CharField('Product name', max_length=60)
    text = models.TextField('Product text')
    img1 = models.ImageField('Product image1', upload_to='images')
    img2 = models.ImageField('Product image2', upload_to='images')

    def __str__(self):
        return self.name
            
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class AboutClient(models.Model):

    name = models.CharField('About Client name', max_length=60)
    text = models.TextField('About Client text')

    def __str__(self):
        return self.name
            
    class Meta:
        verbose_name = 'AboutClient'
        verbose_name_plural = 'AboutClients'

class Client(models.Model):

    link = models.URLField('Client link')
    img = models.ImageField('Client image', upload_to='images')

            
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Contact(models.Model):

    contact_name = models.CharField('Contact name', max_length=60)
    contact_email = models.EmailField('Contact email')
    contact_message = models.TextField('Contact text')

    def __str__(self):
        return self.contact_name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'