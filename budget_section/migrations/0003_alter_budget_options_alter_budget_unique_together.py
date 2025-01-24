# Generated by Django 4.1.7 on 2024-12-03 03:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget_section', '0002_alter_category_slug_alter_category_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budget',
            options={'verbose_name_plural': 'Budgets'},
        ),
        migrations.AlterUniqueTogether(
            name='budget',
            unique_together={('user', 'slug'), ('user', 'name')},
        ),
    ]
