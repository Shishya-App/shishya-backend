from django.contrib import admin

# Register your models here.
from userpanel.models import CustomDocumentUploadModel, ProfileDocumentModel

admin.site.register(CustomDocumentUploadModel)
admin.site.register(ProfileDocumentModel)