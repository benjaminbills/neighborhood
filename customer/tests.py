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
  def test_update_profile(self):
      self.profile.save_profile()
      self.profile.update_profile(self.profile.id, bio='I am good', photo='http:image2')
      update_bio=Profile.objects.get(bio='I am good')
      update_profile_photo=Profile.objects.get(photo='http:image2')
      self.assertEqual(update_bio.bio,'I am good') 
      self.assertEqual(update_profile_photo.photo,'http:image2') 


class NeighborhoodTestClass(TestCase):
  def setUp(self):
      self.neighborhood = Neighborhood(name='Sandalwood', location='karen', occupants_count=10)
  def test_instance(self):
      self.assertTrue(isinstance(self.neighborhood,Neighborhood))
  def test_save_method(self):
      self.neighborhood.save_neighborhood()     
      neighborhood = Neighborhood.objects.all()
      self.assertTrue(len(neighborhood) > 0)  