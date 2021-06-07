from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    neighborhood_desc=models.TextField() 
    occupants_count=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
      
    def save_neighborhood(self):
      self.save()
      
    def delete_neighborhood(self):
      self.delete()  
      
    @classmethod
    def find_neighborhood(cls, name):
      return cls.objects.filter(name_icontains=name) 
    
    @classmethod
    def update_neighborhood(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update 

class Profile(models.Model):
  photo=models.ImageField(upload_to='profile_photos/', default='profile_photos/default_rr8opn', blank=True)
  bio=models.TextField(max_length=1000, default='No Bio')
  user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
  
  def save_profile(self):
        self.save()
  def delete_profile(self):
        self.delete()
  @classmethod
  def update_profile(cls, profile_id, bio, photo):
        profile = cls.objects.filter(pk=profile_id).update(bio=bio,photo=photo)
        return profile
  @classmethod
  def get_profile(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile