# Generated by Django 3.2.11 on 2022-02-09 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basketapp", "0003_auto_20220203_2209"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="basket",
            options={"ordering": ("id",)},
        ),
    ]
