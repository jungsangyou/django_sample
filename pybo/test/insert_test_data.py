from django.test import TestCase

from pybo.models import Question
from django.utils import timezone

class Insert_test_data(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print(11)
        for i in range(300): 
            
            test_question = Question.objects.create(subject='테스트 데이터 입니다:[%03d]' % i , content='내용무 [%03d]' % i, create_date=timezone.now())
            print(test_question)

    def test_inset_data(self):
        
        self.assertTrue(True)