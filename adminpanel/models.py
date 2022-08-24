from django.db import models

# Create your models here.
from base.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class SSC(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class HSC(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class MigrationCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class JEEmarksheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class JEEallotmentLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class DisabilityCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class DomicileCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class PAN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class BirthCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
    
class Passport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class SportsCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class TransferCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class CasteCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class  IncomeCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class  MedicalCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    
class  NationalityCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PrivateKey= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    

class DocumentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SSC = models.ForeignKey(SSC, on_delete=models.CASCADE, blank=True, null=True)
    HSC = models.ForeignKey(HSC, on_delete=models.CASCADE, blank=True, null=True)
    MigrationCertificate = models.ForeignKey(MigrationCertificate, on_delete=models.CASCADE, blank=True, null=True)
    JEEmarksheet = models.ForeignKey(JEEmarksheet, on_delete=models.CASCADE, blank=True, null= True)
    JEEallotmentLetter = models.ForeignKey(JEEallotmentLetter, on_delete=models.CASCADE, blank=True, null= True)
    DisabilityCertificate = models.ForeignKey(DisabilityCertificate, on_delete=models.CASCADE, blank=True, null= True)
    DomicileCertificate = models.ForeignKey(DomicileCertificate, on_delete=models.CASCADE, blank=True, null= True)
    PAN = models.ForeignKey(PAN, on_delete=models.CASCADE, blank=True, null= True)
    BirthCertificate = models.ForeignKey(BirthCertificate, on_delete=models.CASCADE, blank=True, null= True)
    SportsCertificate = models.ForeignKey(SportsCertificate, on_delete=models.CASCADE, blank=True, null= True)
    TransferCertificate = models.ForeignKey(TransferCertificate, on_delete=models.CASCADE, blank=True, null= True)
    CasteCertificate = models.ForeignKey(CasteCertificate, on_delete=models.CASCADE, blank=True, null= True)
    Passport = models.ForeignKey(Passport, on_delete=models.CASCADE, blank=True, null= True)
    IncomeCertificate = models.ForeignKey(IncomeCertificate, on_delete=models.CASCADE, blank=True, null= True)
    MedicalCertificate = models.ForeignKey(MedicalCertificate, on_delete=models.CASCADE, blank=True, null= True)
    NationalityCertificate = models.ForeignKey(NationalityCertificate, on_delete=models.CASCADE, blank=True, null= True)
    
    def __str__(self):
        return self.user.email
    

class PersonalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    age= models.IntegerField(blank=False)
    documentField= models.ForeignKey(DocumentModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Form(models.Model):

    class Meta:
        verbose_name = _("Form")
        verbose_name_plural = _("Forms")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Form"), verbose_name=_("Form Title"))
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.id) + "_" + str(self.title))


class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(models.Model):

    form = models.ForeignKey(
        Form, related_name='question', on_delete=models.CASCADE, verbose_name=_("Form.id"))
    
    TYPE = (
        ('mcq_one', 'MCQ with single possible answer'),
        ('text', 'Text based answer'),
        ('file_upload', 'File Upload answer')
    )
    
    technique = models.CharField(
       max_length=55, choices=TYPE)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text
    
class TextAnswer(Answer):
    answer_text = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)


class McqOneAnswer(Answer):
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice.choice_text
    
class FileUploadAnswer(Answer):
    File= models.FileField(upload_to ="my_documents",blank=True)
    
    def __str__(self):
        return str(self.id)