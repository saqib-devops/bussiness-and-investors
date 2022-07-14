# Generated by Django 3.2 on 2022-07-14 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='business/profile/')),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=False)),
                ('cro', models.CharField(max_length=200)),
                ('registration_number', models.CharField(max_length=200)),
                ('registration_date', models.DateTimeField(null=True)),
                ('mandatory_filling', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=20)),
                ('phone_no', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='investor/profiles')),
                ('nationality', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='projects/')),
                ('cro', models.CharField(max_length=200)),
                ('registration_number', models.CharField(max_length=200)),
                ('registration_date', models.DateTimeField(null=True)),
                ('website', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.category')),
            ],
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('equity', 'Equity')], default='equity', max_length=20)),
                ('value', models.PositiveIntegerField(default=0)),
                ('percentage_equity', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('sell_equity', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_project', to='business.project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
                ('percentage_equity', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('is_agree', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.investor')),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.shares')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('project_investor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.project_investor')),
            ],
        ),
        migrations.CreateModel(
            name='MoneyFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_profit_project', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('business_loss_project', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('investor_profit', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('investor_loss', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('monthly_cost', models.IntegerField(default=0)),
                ('monthly_earning', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.project')),
                ('project_investor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.project_investor')),
            ],
        ),
        migrations.CreateModel(
            name='InvestorShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
                ('percentage_equity', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.project_investor')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.category'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
