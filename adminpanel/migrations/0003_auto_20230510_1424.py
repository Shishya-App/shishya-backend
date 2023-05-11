# Generated by Django 3.2.19 on 2023-05-10 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpanel', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('nature', models.CharField(choices=[('intern', 'Intern'), ('contract', 'Contract'), ('fulltime', 'Full-Time')], max_length=255)),
                ('deadline', models.DateField()),
                ('salary_range_min', models.IntegerField(blank=True, null=True)),
                ('salary_range_max', models.IntegerField(blank=True, null=True)),
                ('job_location', models.CharField(choices=[('andhra-pradesh', 'Andhra Pradesh'), ('arunachal-pradesh', 'Arunachal Pradesh'), ('assam', 'Assam'), ('bihar', 'Bihar'), ('chhattisgarh', 'Chhattisgarh'), ('goa', 'Goa'), ('gujarat', 'Gujarat'), ('haryana', 'Haryana'), ('himachal-pradesh', 'Himachal Pradesh'), ('jammu-and-kashmir', 'Jammu and Kashmir'), ('jharkhand', 'Jharkhand'), ('karnataka', 'Karnataka'), ('kerala', 'Kerala'), ('madhya-pradesh', 'Madhya Pradesh'), ('maharashtra', 'Maharashtra'), ('manipur', 'Manipur'), ('meghalaya', 'Meghalaya'), ('mizoram', 'Mizoram'), ('nagaland', 'Nagaland'), ('odisha', 'Odisha'), ('punjab', 'Punjab'), ('rajasthan', 'Rajasthan'), ('sikkim', 'Sikkim'), ('tamil-nadu', 'Tamil Nadu'), ('telangana', 'Telangana'), ('tripura', 'Tripura'), ('uttar-pradesh', 'Uttar Pradesh'), ('uttarakhand', 'Uttarakhand'), ('west-bengal', 'West Bengal')], max_length=55)),
                ('jd', models.TextField()),
                ('eligibilty', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='JobQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technique', models.CharField(choices=[('text', 'Text based answer'), ('file_upload', 'File Upload answer'), ('pre_verified', 'Auto Upload answer')], max_length=55)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='adminpanel.job', verbose_name='Job.id')),
            ],
        ),
        migrations.RemoveField(
            model_name='mcqoneanswer',
            name='answer_ptr',
        ),
        migrations.RemoveField(
            model_name='mcqoneanswer',
            name='choice',
        ),
        migrations.RenameField(
            model_name='adhaarfile',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='birthcertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='castecertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='disabilitycertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='domicilecertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='hsc',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='incomecertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='jeeallotmentletter',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='jeemarksheet',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='medicalcertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='migrationcertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='nationalitycertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='pan',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='passport',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='sportscertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='ssc',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RenameField(
            model_name='transfercertificate',
            old_name='PrivateKey',
            new_name='Private_key',
        ),
        migrations.RemoveField(
            model_name='adhaarfile',
            name='File',
        ),
        migrations.RemoveField(
            model_name='birthcertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='castecertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='disabilitycertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='domicilecertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='hsc',
            name='File',
        ),
        migrations.RemoveField(
            model_name='incomecertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='jeeallotmentletter',
            name='File',
        ),
        migrations.RemoveField(
            model_name='jeemarksheet',
            name='File',
        ),
        migrations.RemoveField(
            model_name='medicalcertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='migrationcertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='nationalitycertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='pan',
            name='File',
        ),
        migrations.RemoveField(
            model_name='passport',
            name='File',
        ),
        migrations.RemoveField(
            model_name='sportscertificate',
            name='File',
        ),
        migrations.RemoveField(
            model_name='ssc',
            name='File',
        ),
        migrations.RemoveField(
            model_name='transfercertificate',
            name='File',
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='AdhaarFile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.adhaarfile'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='BirthCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.birthcertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='CasteCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.castecertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='DisabilityCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.disabilitycertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='DomicileCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.domicilecertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='HSC',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.hsc'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='IncomeCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.incomecertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='JEEallotmentLetter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.jeeallotmentletter'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='JEEmarksheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.jeemarksheet'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='MedicalCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.medicalcertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='MigrationCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.migrationcertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='NationalityCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.nationalitycertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='PAN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.pan'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='Passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.passport'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='SSC',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.ssc'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='SportsCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.sportscertificate'),
        ),
        migrations.AlterField(
            model_name='documentmodel',
            name='TransferCertificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.transfercertificate'),
        ),
        migrations.CreateModel(
            name='JobFileUploadAnswer',
            fields=[
                ('jobanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='adminpanel.jobanswer')),
                ('File', models.FileField(blank=True, upload_to='docs')),
            ],
            options={
                'abstract': False,
            },
            bases=('adminpanel.jobanswer',),
        ),
        migrations.CreateModel(
            name='JobPreVerifiedAnswer',
            fields=[
                ('jobanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='adminpanel.jobanswer')),
                ('doc_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('adminpanel.jobanswer',),
        ),
        migrations.CreateModel(
            name='JobTextAnswer',
            fields=[
                ('jobanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='adminpanel.jobanswer')),
                ('answer_text', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('adminpanel.jobanswer',),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='McqOneAnswer',
        ),
        migrations.AddField(
            model_name='jobanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='adminpanel.jobquestion'),
        ),
    ]