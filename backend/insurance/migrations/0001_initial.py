# Generated by Django 3.2.12 on 2022-09-27 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cover_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Detail_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.IntegerField()),
                ('species', models.IntegerField()),
                ('animal_name', models.CharField(max_length=100)),
                ('animal_birth', models.IntegerField()),
                ('outpatient', models.IntegerField(null=True)),
                ('hospitalization', models.IntegerField(null=True)),
                ('operation', models.IntegerField(null=True)),
                ('patella', models.IntegerField(null=True)),
                ('skin_disease', models.IntegerField(null=True)),
                ('dental', models.IntegerField(null=True)),
                ('urinary', models.IntegerField(null=True)),
                ('liability', models.IntegerField(null=True)),
                ('insurance_choice', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('insurance_name', models.CharField(max_length=100)),
                ('species', models.IntegerField()),
                ('company_score', models.FloatField()),
                ('company_url', models.CharField(max_length=300)),
                ('company_logo', models.CharField(max_length=200)),
                ('renewal', models.BooleanField(default=False)),
                ('payment_period', models.IntegerField()),
                ('content', models.TextField(null=True)),
                ('etc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
                ('basic', models.JSONField(null=True)),
                ('special', models.JSONField(null=True)),
                ('all_cover', models.JSONField(null=True)),
                ('content', models.TextField(null=True)),
                ('price_score', models.FloatField()),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_detail', to='insurance.insurance')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=300, null=True)),
                ('score', models.IntegerField()),
                ('detail_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='insurance.detail_user')),
                ('insurance_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='insurance.insurance_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('content', models.TextField()),
                ('item_url', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('cover_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='insurance.cover_type')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('tip', models.TextField()),
                ('cause', models.TextField()),
                ('cover_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disease', to='insurance.cover_type')),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('wild', models.BooleanField(default=False, null=True)),
                ('detail', models.TextField()),
                ('cover_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='insurance.cover_type')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='insurance.insurance')),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('wild', models.BooleanField(default=False)),
                ('disease', models.ManyToManyField(related_name='breed', to='insurance.Disease')),
            ],
        ),
    ]
