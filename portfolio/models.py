from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100, blank=True)
    description=models.CharField(max_length=250)
    #image=models.ImageField(upload_to='portfolio/images')
    url=models.URLField(blank=True)
    technology=models.CharField(max_length=250, default='0000000')

    def __str__(self):
        return self.title


class PhotoResume(models.Model):
    my_photo=models.ImageField(upload_to='portfolio/personal_files')
    resume=models.FileField(upload_to='portfolio/personal_files', blank=True)

    # def __str__(self):
    #     return self.


