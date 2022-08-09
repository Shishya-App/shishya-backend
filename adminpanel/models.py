from django.db import models

# Create your models here.
from base.models import User

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
    SSC = models.ForeignKey(SSC, on_delete=models.CASCADE)
    HSC = models.ForeignKey(HSC, on_delete=models.CASCADE)
    MigrationCertificate = models.ForeignKey(MigrationCertificate, on_delete=models.CASCADE)
    JEEmarksheet = models.ForeignKey(JEEmarksheet, on_delete=models.CASCADE)
    JEEallotmentLetter = models.ForeignKey(JEEallotmentLetter, on_delete=models.CASCADE)
    DisabilityCertificate = models.ForeignKey(DisabilityCertificate, on_delete=models.CASCADE)
    DomicileCertificate = models.ForeignKey(DomicileCertificate, on_delete=models.CASCADE)
    PAN = models.ForeignKey(PAN, on_delete=models.CASCADE)
    BirthCertificate = models.ForeignKey(BirthCertificate, on_delete=models.CASCADE)
    SportsCertificate = models.ForeignKey(SportsCertificate, on_delete=models.CASCADE)
    TransferCertificate = models.ForeignKey(TransferCertificate, on_delete=models.CASCADE)
    CasteCertificate = models.ForeignKey(CasteCertificate, on_delete=models.CASCADE)
    Passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    IncomeCertificate = models.ForeignKey(IncomeCertificate, on_delete=models.CASCADE)
    MedicalCertificate = models.ForeignKey(MedicalCertificate, on_delete=models.CASCADE)
    NationalityCertificate = models.ForeignKey(NationalityCertificate, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
    

class PersonalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    age= models.IntegerField(blank=False)
    documentField= models.ForeignKey(DocumentModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name