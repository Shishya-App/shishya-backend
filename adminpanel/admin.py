from django.contrib import admin

from adminpanel.models import (HSC, PAN, SSC, BirthCertificate,
                               CasteCertificate, DisabilityCertificate,
                               DocumentModel, DomicileCertificate,
                               IncomeCertificate, JEEallotmentLetter,
                               JEEmarksheet, MedicalCertificate,
                               MigrationCertificate, NationalityCertificate,
                               Passport, PersonalDetails, Question,
                               SportsCertificate, TransferCertificate,
                               Category,Form)

admin.site.register(PersonalDetails)
admin.site.register(SSC)
admin.site.register(HSC)
admin.site.register(MigrationCertificate)
admin.site.register(JEEmarksheet)
admin.site.register(JEEallotmentLetter)
admin.site.register(DisabilityCertificate)
admin.site.register(CasteCertificate)
admin.site.register(DomicileCertificate)
admin.site.register(PAN)
admin.site.register(BirthCertificate)
admin.site.register(Passport)
admin.site.register(SportsCertificate)
admin.site.register(TransferCertificate)
admin.site.register(IncomeCertificate)
admin.site.register(MedicalCertificate)
admin.site.register(NationalityCertificate)
admin.site.register(DocumentModel)
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(Category)
