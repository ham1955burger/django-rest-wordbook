from django.db import models
from sorl.thumbnail import delete

class Word(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100)
    mean = models.CharField(max_length=100)
    example = models.TextField()
    image = models.ImageField()
    # image = models.ImageField(upload_to='%Y/%m/%d')

    class Meta:
        ordering = ('created', )

    def delete(self, *args, **kwargs):
        # 순서주의! cached db에서 지워준 후, 본 db에서 삭제
        delete(self.image)
        # 파일 경로에 있는 사진 제거
        self.image.delete()
        super(Word, self).delete(*args, **kwargs)
