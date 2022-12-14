# Generated by Django 4.1.2 on 2022-10-25 16:10

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="applets",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.RichTextBlock()),
                    ("video", wagtail.images.blocks.ImageChooserBlock()),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
