from django.contrib import admin

# Register your models here.
from userpanel.models import CustomDocumentUploadModel, ProfileDocumentModel, SubmitPreVerifiedQuestion

admin.site.register(CustomDocumentUploadModel)
admin.site.register(ProfileDocumentModel)
admin.site.register(SubmitPreVerifiedQuestion)