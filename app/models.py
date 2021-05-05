from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
    
class About(models.Model):
    sno = models.AutoField(primary_key=True)
    head = models.TextField()
    heading = models.CharField(max_length=100)
    description = models.TextField()

class Fact(models.Model):
    sno = models.AutoField(primary_key=True)
    fact_icon = models.CharField(max_length=50)
    fact = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description

class Skill(models.Model):
    sno = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=50)
    level = models.CharField(max_length=10)
    def __str__(self):
        return self.skill

class Summary(models.Model):
    summary = models.TextField()

class Education(models.Model):
    sno = models.AutoField(primary_key=True)
    course = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    institute = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.course

class Professional(models.Model):
    sno = models.AutoField(primary_key=True)
    work = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    company = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.work
    
class Application(models.Model):
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True) 
    client = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def imageURL(self): 
        try:
            url = self.image.url  
        except:
            url = ''
        return url

    @property
    def image2URL(self): 
        try:
            url = self.image2.url  
        except:
            url = ''
        return url

    @property
    def image3URL(self): 
        try:
            url = self.image3.url  
        except:
            url = ''
        return url

class Startup(models.Model):
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True, null=True)
    client = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def imageURL(self): 
        try:
            url = self.image.url 
        except:
            url = ''
        return url 
    
    @property
    def image2URL(self): 
        try:
            url = self.image2.url  
        except:
            url = ''
        return url

    @property
    def image3URL(self): 
        try:
            url = self.image3.url  
        except:
            url = ''
        return url

class Web(models.Model):
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True, null=True)
    client = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

    @property
    def image2URL(self): 
        try:
            url = self.image2.url  
        except:
            url = ''
        return url

    @property
    def image3URL(self): 
        try:
            url = self.image3.url  
        except:
            url = ''
        return url

class Service(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    title_url = models.URLField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    github = models.URLField(max_length=100)
    youtube = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)

class Profile(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    address_url = models.URLField(max_length=500)

    def __str__(self):
        return self.name

    @property
    def imageURL(self): 
        try:
            url = self.image.url     
        except:
            url = ''
        return url 
    
