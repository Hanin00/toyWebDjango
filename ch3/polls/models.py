from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date created')
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    # 외래키, 원본 테이블의 tuple 삭제시 같이 삭제됨
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.answer_text