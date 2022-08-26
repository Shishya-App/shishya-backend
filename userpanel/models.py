from django.db import models
from base.models import User
from adminpanel.models import DocumentModel, FileUploadAnswer, Question
# Create your models here.

class CustomDocumentUploadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PagesNo = models.IntegerField()
    Title = models.CharField(max_length=200)
    isVerified = models.BooleanField(default=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class ProfileDocumentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NAD_Documents= models.ForeignKey(DocumentModel, on_delete=models.CASCADE)
    
class SubmitFileQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.FileField(upload_to ="docs",blank=True)
    form = models.IntegerField()
    
class SubmitPreVerifiedQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null= True, blank= True)
    form = models.IntegerField()
    question = models.IntegerField()
    file_id = models.IntegerField(null=True, blank=True)
    
# class SubmitMCQQuestion(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.FileField(upload_to ="docs",blank=True)

class SubmitTextQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)
    