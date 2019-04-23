import unittest
from app.models import Pitch

class NewsTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Pitch class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_pitch = Pitch(1 ,'New','New','New','New',0,0,'New','New')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_pitch, Pitch))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_pitch.id, 1)
            self.assertEquals(self.new_pitch.title, 'New')
            self.assertEquals(self.new_pitch.description, 'New')
            self.assertEquals(self.new_pitch.category, 'New')
            self.assertEquals(self.new_pitch.comments, 'New')
            self.assertEquals(self.new_pitch.upvotes, 0)
            self.assertEquals(self.new_pitch.downvotes, 0)
            self.assertEquals(self.new_pitch.posted_p, 'New')
            self.assertEquals(self.new_pitch.user_p, 'New')




if __name__ == '__main__':
    unittest.main()