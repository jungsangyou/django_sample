from django.utils import timezone

from pybo.models import Question,Answer


q = Question(subject='pybo가 무었인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
q.save()

a = Answer(question=q, content="네 자동으로 생성 됩니다.", create_date=timezone.now())
a.save()