from django.db import models

# Create your models here.
class Board(models.Model):
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# author : 작성자 이름이 저장되는 필드입니다.
# 최대 길이를 10으로 제한하였습니다.
# null 값이 저장될 수 없습니다.
# title : 글 제목이 저장되는 필드입니다.
# 최대 길이를 100으로 제한하였습니다.
# null 값이 저장될 수 없습니다.
# content : 내용이 저장되는 필드입니다.
# 앞의 author, title과 다르게 TextField로 되어있어 많은 Text를 써넣을 수 있습니다.
# null 값이 저장될 수 없습니다.
# created_date : 게시물이 생성된 시간이 저장되는 필드입니다. (auto_now_add=True)
# modified_date : 게시물이 수정된 시간이 저장되는 필드입니다. (auto_now=True)