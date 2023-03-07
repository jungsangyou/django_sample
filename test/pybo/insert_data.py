import sys, os

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from pybo.models import Question

from django.utils import timezone


def main():
    for i in range(300):
        q = Question(subject="테스트 데이터 입니다:[%03d]" %i , content='내용 무', create_date=timezone.now())
        q.save()
        
        
if __name__ == '__main__' :
    main()