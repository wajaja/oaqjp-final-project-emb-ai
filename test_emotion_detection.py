# Import the 'unittest' module to create unit tests for your code.
import unittest

from emotion_detection import emotion_detector

class TestEmotion(unittest.TestCase): 
   
    def test1(self): 
        
        self.assertEqual(emotion_detector("I am glad this happened"), "joy") 
        
        self.assertEqual(emotion_detector("I am really mad about this"), "anger") 

        self.assertEqual(emotion_detector("I feel disgusted just hearing about this"), "") 
        
        self.assertEqual(emotion_detector("I am so sad about this"), "disgust") 

        self.assertEqual(emotion_detector("I am really afraid that this will happen"), "fear") 
        
        #self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
      

unittest.main()
