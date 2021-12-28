from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # to dlt profile when dlt user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    




# in the shell terminal we can access users and profiles like this:
# from django.contrib.auth.models import User
# user = User.object.filter(username='alaa').first() // store it (user) in variable 
# user ===== will give us the username we demanded
# user.profile
# user.profile.image
# user.profile.image.width/height....etc
# user.profile.image.url (image location)
