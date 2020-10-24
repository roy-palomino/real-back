# Generated by Django 3.1.2 on 2020-10-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_usersubscription_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='documentdetail',
            old_name='document_id',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='download',
            old_name='document_id',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='download',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='paypal_id',
            new_name='paypal',
        ),
        migrations.RenameField(
            model_name='usersubscription',
            old_name='payment_id',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='usersubscription',
            old_name='subscription_id',
            new_name='subscription',
        ),
        migrations.RenameField(
            model_name='usersubscription',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]