# Generated by Django 4.1.4 on 2022-12-20 10:08

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0018_alter_homepage_applets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="applets",
            field=wagtail.fields.StreamField(
                [
                    (
                        "button_applet",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                ("url", wagtail.blocks.URLBlock()),
                            ]
                        ),
                    ),
                    (
                        "contact_applet",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                ("email", wagtail.blocks.EmailBlock()),
                            ]
                        ),
                    ),
                    (
                        "notes_applet",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "notes",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("title", wagtail.blocks.CharBlock()),
                                                (
                                                    "content",
                                                    wagtail.blocks.RichTextBlock(
                                                        features=[
                                                            "h2",
                                                            "bold",
                                                            "italic",
                                                            "link",
                                                        ]
                                                    ),
                                                ),
                                            ],
                                            label="notes",
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "pomodoro_applet",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock(max_length=20))]
                        ),
                    ),
                    (
                        "calendar_applet",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock(max_length=20))]
                        ),
                    ),
                    (
                        "social_links_applet",
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
                                            label="links",
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "textual_applet",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "content",
                                    wagtail.blocks.RichTextBlock(
                                        features=["h2", "bold", "italic", "link"]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "timeline_applet",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "events",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("date", wagtail.blocks.DateBlock()),
                                                ("title", wagtail.blocks.CharBlock()),
                                                (
                                                    "description",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                            ],
                                            label="events",
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "todo_applet",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=20)),
                                (
                                    "tasks",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(), label="tasks"
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
