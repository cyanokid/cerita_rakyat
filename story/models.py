from django.db import models
from django.contrib.auth.models import User #django built in user
from django.db.models.signals import post_save #signal to post something then do something
# from django.dispatch import receiver ##or use this

# Create your models here.
class Story(models.Model):
    username = models.CharField('Username', max_length=120)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField('Email Address', blank=True)
    title = models.CharField('Tittle', max_length=120)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #approval
    #by default it is false
    approved = models.BooleanField('Approved', default=False)
    #many user can likes many story
    likes = models.ManyToManyField(User, related_name="story_like", blank=True)
    sads = models.ManyToManyField(User, related_name="story_sad", blank=True)
    laughs = models.ManyToManyField(User, related_name="story_laugh", blank=True)
    angrys = models.ManyToManyField(User, related_name="story_angry", blank=True)
    shocks = models.ManyToManyField(User, related_name="story_shock", blank=True)

    # keep track or count the likes
    def number_of_likes(self):
        return self.likes.count()

    # keep track or count the sad
    def number_of_sads(self):
        return self.sads.count()

    # keep track or count the laughs
    def number_of_laughs(self):
        return self.laughs.count()
    
    # keep track or count the angrys
    def number_of_angrys(self):
        return self.angrys.count()
    
    # keep track or count the shocks
    def number_of_shocks(self):
        return self.shocks.count()
        
    

    def __str__(self):
        return self.title
    
    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y at %I:%M %p')

# Create Profile models here.
class Profile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    date_modified = models.DateTimeField(User, auto_now=True)   # To get last time update
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    
    #to display on admin 
    def __str__(self):
        return self.user.username

# Automatically create profile when user sign up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)





