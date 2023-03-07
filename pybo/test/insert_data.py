import sys, os
import django
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_crazy_service.settings')
django.setup()

from pybo.models import Question
from django.utils import timezone


for i in range(300):
        q = Question(subject="테스트 데이터 입니다:[%03d]" %i , content='내용 무', create_date=timezone.now())
        q.save()