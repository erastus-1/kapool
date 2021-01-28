from django.test import TestCase
from .models import Profile,Car,Uber,Passenger,Category
from django.contrib.auth.models import User



# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        user1=User(first_name="Erastus",last_name="Kariuki")
        self.person1=Profile(username='Erastus',user_type='Driver',user=user1)
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.person1,Profile))
   

class PassengerTestClass(TestCase):
    def setUp(self):
        user2=User(first_name="Passenger",)
        profile1=Profile(username='Passenger',user_type='passenger',user=user2)

    def test_instance(self):
        self.assertTrue(isinstance(self.passenger,Passenger))
    
    def test_string_rep(self):
        user2=User(first_name="Passenger")
        profile1=Profile(username='Passenger',user_type='passenger',user=user2)
        self.assertEqual(self.passenger.name,"Passenger")
        