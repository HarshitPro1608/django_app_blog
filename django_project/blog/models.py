from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.IT IS USED TO CREATE CLASSES TO BE ADDED TO DATABASE. FOR DATABASE CHANGES RUN MIGRATIONS
# First after making changes run python manage.py makemigrations and then run python manage.py sqlmigrate appname migration number from migrations folder(blog 0001) and then python manage.py migrate
#python manage.py shell(to open db)>>> from blog.models import Post
#>>> from django.contrib.auth.models import User User.objects.all/first/filter(username='Harshit')/filter(..).first(),store it in user= and then do user.id/pk, then create post like post_1=Post(title='Blog 1',content=....,author=user),post_1.save()
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)#ON DELETING USER POSTS WILL ALSO DELETE
#to get all user post run user.post(modelname)_set.all()/.create(title=...)
    def __str__(self):#returns title on query set
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})#to redirect to post-detail url after post creation. Note reverse use and not redirect 
    