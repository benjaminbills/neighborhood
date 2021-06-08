from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighborhood, Profile

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.neighborhood = Neighborhood(name='Sandalwood', location='karen', occupants_count=10)
      self.user.save()
      self.neighborhood.save()
      self.profile = Profile(photo='http:cloudinary/devward/profile/ben.jpg', bio='I am amazing', user=self.user, neighborhood=self.neighborhood)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.profile,Profile))  
  def test_save_method(self):
      self.profile.save_profile()     
      profile = Profile.objects.all()
      self.assertTrue(len(profile) > 0) 
  def tearDown(self):
      Profile.objects.all().delete()
  def delete_profile(self):
      self.profile.save_profile()
      profile=Profile.objects.all()
      self.assertEqual(len(profile), 1) 
      self.profile.delete_profile()
      del_profile=Profile.objects.all()
      self.assertEqual(len(del_profile),0)
