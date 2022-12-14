# Generated by Django 4.1.2 on 2022-10-26 16:46

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_applets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="applets",
            field=wagtail.fields.StreamField(
                [
                    (
                        "textual",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(
                                        features=["bold", "italic", "link"],
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                ("media", wagtail.embeds.blocks.EmbedBlock()),
                            ]
                        ),
                    ),
                    (
                        "social",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "links",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("title", wagtail.blocks.CharBlock()),
                                                ("url", wagtail.blocks.URLBlock()),
                                            ],
                                            label="link",
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "todo",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "tasks",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(label="task")
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
