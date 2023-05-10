from django.db import models

# Create your models here.
from base.models import User
from django.utils.translation import gettext_lazy as _

class PersonalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    age= models.IntegerField(blank=True, null=True)
    documentField= models.ForeignKey('adminpanel.DocumentModel', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class DocumentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SSC = models.ForeignKey('adminpanel.SSC', on_delete=models.DO_NOTHING, blank=True, null=True)
    HSC = models.ForeignKey('adminpanel.HSC', on_delete=models.DO_NOTHING, blank=True, null=True)
    AdhaarFile = models.ForeignKey('adminpanel.AdhaarFile', on_delete=models.DO_NOTHING, blank=True, null=True)
    MigrationCertificate = models.ForeignKey('adminpanel.MigrationCertificate', on_delete=models.DO_NOTHING, blank=True, null=True)
    JEEmarksheet = models.ForeignKey('adminpanel.JEEmarksheet', on_delete=models.DO_NOTHING, blank=True, null= True)
    JEEallotmentLetter = models.ForeignKey('adminpanel.JEEallotmentLetter', on_delete=models.DO_NOTHING, blank=True, null= True)
    DisabilityCertificate = models.ForeignKey('adminpanel.DisabilityCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    DomicileCertificate = models.ForeignKey('adminpanel.DomicileCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    PAN = models.ForeignKey('adminpanel.PAN', on_delete=models.DO_NOTHING, blank=True, null= True)
    BirthCertificate = models.ForeignKey('adminpanel.BirthCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    SportsCertificate = models.ForeignKey('adminpanel.SportsCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    TransferCertificate = models.ForeignKey('adminpanel.TransferCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    CasteCertificate = models.ForeignKey('adminpanel.CasteCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    Passport = models.ForeignKey('adminpanel.Passport', on_delete=models.DO_NOTHING, blank=True, null= True)
    IncomeCertificate = models.ForeignKey('adminpanel.IncomeCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    MedicalCertificate = models.ForeignKey('adminpanel.MedicalCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    NationalityCertificate = models.ForeignKey('adminpanel.NationalityCertificate', on_delete=models.DO_NOTHING, blank=True, null= True)
    
    def __str__(self):
        return self.user.email
    
    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         super().save(*args, **kwargs)
    #         personal_details, created = PersonalDetails.objects.get_or_create(user=self.user)
    #         personal_details.documentField = self
    #         personal_details.save()
    #     else:
    #         return super().save()

class AdhaarFile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.AdhaarFile = self
            document_model.save()
        else:
            return super().save()
        
class Adhaar(models.Model):
    adhaar_no = models.CharField(max_length=255, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    dob = models.DateField(auto_now_add=True, blank=True)
    gender = models.CharField(max_length=255, blank=True)

class SSC(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.SSC = self
            document_model.save()
        else:
            return super().save()
    
    
class HSC(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.HSC = self
            document_model.save()
        else:
            return super().save()   
    
class MigrationCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.MigrationCertificate = self
            document_model.save()
        else:
            return super().save()
    
    
class JEEmarksheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.JEEmarksheet = self
            document_model.save()
        else:
            return super().save()
        
class JEEallotmentLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.JEEallotmentLetter = self
            document_model.save()
        else:
            return super().save()        
    
    
class DisabilityCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.DisabilityCertificate = self
            document_model.save()
        else:
            return super().save()     
    
    
class DomicileCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.DomicileCertificate = self
            document_model.save()
        else:
            return super().save()    
    
    
class PAN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.PAN = self
            document_model.save()
        else:
            return super().save()    
    
    
class BirthCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.BirthCertificate = self
            document_model.save()
        else:
            return super().save()  
    
class Passport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.Passport = self
            document_model.save()
        else:
            return super().save() 
    
class SportsCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.SportsCertificate = self
            document_model.save()
        else:
            return super().save()      
    
class TransferCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.TransferCertificate = self
            document_model.save()
        else:
            return super().save()         
    
class CasteCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.CasteCertificate = self
            document_model.save()
        else:
            return super().save()       
    
class  IncomeCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
  
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.IncomeCertificate = self
            document_model.save()
        else:
            return super().save()       
    
class  MedicalCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="docs",blank=True)
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.MedicalCertificate = self
            document_model.save()
        else:
            return super().save() 
    
class  NationalityCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    Private_key= models.CharField(max_length=500, blank=True)
    isVerified= models.BooleanField(default=True)
    File= models.FileField(upload_to ="docs",blank=True)
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            document_model, created = DocumentModel.objects.get_or_create(user=self.user)
            document_model.NationalityCertificate = self
            document_model.save()
        else:
            return super().save()

    
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
    deadline = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    academic_year  = models.IntegerField(null=True, blank=True)

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
        ('file_upload', 'File Upload answer'),
        ('pre_verified', 'Auto Upload answer'),
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
    
class JobQuestion(models.Model):

    job = models.ForeignKey(
        'adminpanel.Job', related_name='question', on_delete=models.CASCADE, verbose_name=_("Job.id"))
    
    TYPE = (
        ('text', 'Text based answer'),
        ('file_upload', 'File Upload answer'),
        ('pre_verified', 'Auto Upload answer'),
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


class JobAnswer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        JobQuestion, related_name='answer', on_delete=models.CASCADE)
    
class TextAnswer(Answer):
    answer_text = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)
    
class FileUploadAnswer(Answer):
    File= models.FileField(upload_to ="docs",blank=True)
    
    def __str__(self):
        return str(self.id)
    
class PreVerifiedAnswer(Answer):
    doc_id = models.IntegerField()
    
    def __str__(self):
        return str(self.id)
    
class JobTextAnswer(JobAnswer):
    answer_text = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)
    
class JobFileUploadAnswer(JobAnswer):
    File= models.FileField(upload_to ="docs",blank=True)
    
    def __str__(self):
        return str(self.id)
    
class JobPreVerifiedAnswer(JobAnswer):
    doc_id = models.IntegerField()
    
    def __str__(self):
        return str(self.id)
    
class Job(models.Model):
    TYPE = (
        ('intern', 'Intern'),
        ('contract', 'Contract'),
        ('fulltime', 'Full-Time'),
    )
    
    Location = (
        ('andhra-pradesh', 'Andhra Pradesh'),
        ('arunachal-pradesh', 'Arunachal Pradesh'),
        ('assam', 'Assam'),
        ('bihar', 'Bihar'),
        ('chhattisgarh', 'Chhattisgarh'),
        ('goa', 'Goa'),
        ('gujarat', 'Gujarat'),
        ('haryana', 'Haryana'),
        ('himachal-pradesh', 'Himachal Pradesh'),
        ('jammu-and-kashmir', 'Jammu and Kashmir'),
        ('jharkhand', 'Jharkhand'),
        ('karnataka', 'Karnataka'),
        ('kerala', 'Kerala'),
        ('madhya-pradesh', 'Madhya Pradesh'),
        ('maharashtra', 'Maharashtra'),
        ('manipur', 'Manipur'),
        ('meghalaya', 'Meghalaya'),
        ('mizoram', 'Mizoram'),
        ('nagaland', 'Nagaland'),
        ('odisha', 'Odisha'),
        ('punjab', 'Punjab'),
        ('rajasthan', 'Rajasthan'),
        ('sikkim', 'Sikkim'),
        ('tamil-nadu', 'Tamil Nadu'),
        ('telangana', 'Telangana'),
        ('tripura', 'Tripura'),
        ('uttar-pradesh', 'Uttar Pradesh'),
        ('uttarakhand', 'Uttarakhand'),
        ('west-bengal', 'West Bengal'),
    )
    
    title = models.CharField(max_length=255, null=False, blank=False)
    nature = models.CharField(max_length=255, choices=TYPE, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    salary_range_min = models.IntegerField(null=True, blank=True)
    salary_range_max = models.IntegerField(null=True, blank=True)
    job_location = models.CharField(max_length=55, choices=Location, null=False, blank=False)
    jd = models.TextField(null=False, blank=False)
    eligibilty = models.TextField(null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(str(self.title)+ str(self.id))