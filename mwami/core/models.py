from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='children_photos/')
    sponsored = models.BooleanField(default=False)
def __str__(self):
        return self.Full_name

class Sponsor(models.Model):
    Full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    sponsored_children = models.ManyToManyField(Child, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
     return self.Full_name

class Donation(models.Model):
     sponsor = models.ForeignKey(Sponsor,on_delete=models.SET_NULL, null=True,blank=True)
     amount = models.DecimalField(max_digits = 10, decimal_places=2)
     date_donated = models.DateTimeField(auto_now_add=True)
     Child = models.ForeignKey(Child,on_delete=models.SET_NULL,null=True, blank=True)
     payment_method = models.CharField(
          max_length = 100,
          choices =[('cash', 'Cash'),
                    ('card', 'Card'),
                    ('mobile', 'Mobile payment')
                    ]

     )
     message = models.TextField(blank=True, null=True)
def __str__(self):
     return f"{self.sponsor.Full_name} donated {self.amount} on {self.date.srtftime('%D-%M-%Y')}"


class Volunteer(models.Model):
     Full_name= models.CharField(max_length=100)
     email = models.EmailField()
     phone_number= models.CharField(max_length=20)
     loaction = models.CharField(max_length=100)
     skills = models.TextField(help_text='list your skills or area that you can help with')
     availability=models.TextField(
          max_length=100,
          help_text="Example: weekend,Evening,Full_time, etc"
     )
     joined_date =models.DateTimeField(auto_now_add=True)
     end_date =models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.Full_name

class BlogPost(models.Model):
     title= models.CharField(max_length=250)
     slug =models.SlugField(unique=True)
     author= models.CharField(max_length=100)
     content= models.TextField()
     image=models.ImageField(upload_to='blog_image/')
     created_at= models.DateTimeField(auto_now_add = True)
     is_puplished=models.BooleanField(default=False)
     def __str__(self):
          return self.title
     

class ContactMessage(models.Model):
     name= models.CharField(max_length=100)
     email=models.EmailField()
     subject=models.CharField(max_length=200)
     message=models.TextField()
     sent_at = models.DateTimeField(auto_now_add=True)
     is_read= models.BooleanField(default=False)
     def __str__(self):
          return f"message from {self.name} - {self.subject}"

class ProgressReport(models.Model):
     Child= models.ForeignKey(Child, on_delete=models.CASCADE,related_name='progress_reports')
     report_date=models.DateTimeField(auto_now_add=True)
     title=models.CharField(max_length=200)
     description=models.TextField()
     image=models.ImageField(upload_to='progress_report/')
     added_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f"{self.Child.name} - {self.title} ({self.report_date})"

class MediaContent(models.Model):
     title = models.CharField(max_length=150)
     image = models.ImageField(upload_to='images/',blank=True, null=True)
     video = models.FileField(upload_to='videos/',blank=True, null=True)
     uploaded_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title

class Advertisement(models.Model):
     title = models.CharField(max_length=150)
     image = models.ImageField(upload_to='advertisements/',)
     link = models.URLField(max_length=200, blank=True, null=True)
     is_active = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title
class Slide(models.Model):
     title = models.CharField(max_length=100)
     description =models.TextField()
     image = models.ImageField(upload_to ='slides/')

     def __str__(self):
          return self.title
class HeroSection(models.Model):
     title = models.CharField(max_length=200)
     subtitle = models.TextField()
     background_image = models.ImageField(upload_to='hero/')

     def __str__(self):
          return self.title

class AboutContent(models.Model):
     heading = models.CharField(max_length=100)
     body = models.TextField()
     image = models.ImageField(upload_to='about/')

     def __str__(self):
          return self.heading
class Program(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     icon = models.ImageField(upload_to='programs/')

     def __str__(self):
          return self.name
class ImpactStat(models.Model):
     label = models.CharField(max_length=100)
     value = models.PositiveIntegerField()

     def __str__(self):
          return self.label
class Testimonial(models.Model):
     name = models.CharField(max_length=100)
     quote = models.TextField()
     photo = models.ImageField(upload_to='testimonials/')

     def __str__(self):
          return self.name

class Staff(models.Model):
     name = models.CharField(max_length=100)
     position = models.CharField(max_length=255)
     photo = models.ImageField(upload_to='staff_photos/')
     bio = models.TextField(blank=True, null=True)               



