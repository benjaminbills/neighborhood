from django.test import TestCase
from django.contrib.auth.models import User
from .models import Business, Neighborhood, Post, Profile

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
  def tearDown(self):
      Neighborhood.objects.all().delete()
  def delete_neighborhood(self):
      self.neighborhood.save_neighborhood()
      neighborhood=Neighborhood.objects.all()
      self.assertEqual(len(neighborhood), 1) 
      self.neighborhood.delete_neighborhood()
      del_neighborhood=Neighborhood.objects.all()
      self.assertEqual(len(del_neighborhood),0)
  def test_update_neighborhood(self):
      self.neighborhood.save_neighborhood()
      self.neighborhood.update_neighborhood(self.neighborhood.id, name='Langata', location='ngong', occupants_count=13)
      update_name=Neighborhood.objects.get(name='Langata')
      update_occupant=Neighborhood.objects.get(occupants_count=13)
      self.assertEqual(update_name.name,'Langata') 
      self.assertEqual(update_occupant.occupants_count,13) 


class BusinessTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.neighborhood = Neighborhood(name='Sandalwood', location='karen', occupants_count=10)
      self.user.save()
      self.neighborhood.save()
      self.business = Business(name='Tazama', description='printing center', user=self.user, neighborhood=self.neighborhood)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.business,Business))  
  def test_save_method(self):
      self.business.save_business()     
      business = Business.objects.all()
      self.assertTrue(len(business) > 0) 
  def tearDown(self):
      Business.objects.all().delete()

  def delete_business(self):
      self.business.save_business()
      business=Business.objects.all()
      self.assertEqual(len(business), 1) 
      self.business.delete_business()
      del_business=Business.objects.all()
      self.assertEqual(len(del_business),0)
  def test_update_business(self):
      self.business.save_business()
      self.business.update_business(self.business.id, name='Maliza', email='maliza@gmail.com')
      update_name=Business.objects.get(name='Maliza')
      update_email=Business.objects.get(email='maliza@gmail.com')
      self.assertEqual(update_name.name,'Maliza') 
      self.assertEqual(update_email.email,'maliza@gmail.com') 

class PostTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.neighborhood = Neighborhood(name='Sandalwood', location='karen', occupants_count=10)
      self.user.save()
      self.neighborhood.save()
      self.post = Post(title='Accident', content='accident on road', user=self.user, neighborhood=self.neighborhood)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.post,Post))  
  def test_save_method(self):
      self.post.save_post()     
      post = Post.objects.all()
      self.assertTrue(len(post) > 0) 
  def tearDown(self):
      Post.objects.all().delete()

  