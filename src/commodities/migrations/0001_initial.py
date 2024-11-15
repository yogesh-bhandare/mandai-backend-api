# Generated by Django 5.1.3 on 2024-11-15 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_no', models.CharField(db_index=True, max_length=120, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('commodity', models.CharField(blank=True, max_length=220, null=True)),
                ('quantity', models.CharField(blank=True, max_length=120, null=True)),
                ('income', models.IntegerField(blank=True, default=0, null=True)),
                ('min_price', models.IntegerField(blank=True, default=0, null=True)),
                ('max_price', models.IntegerField(blank=True, default=0, null=True)),
                ('avg_price', models.IntegerField(blank=True, default=0, null=True)),
                ('min_price_per_kg', models.IntegerField(blank=True, default=0, null=True)),
                ('max_price_per_kg', models.IntegerField(blank=True, default=0, null=True)),
                ('avg_price_per_kg', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, help_text='Scrape daily?')),
            ],
        ),
        migrations.CreateModel(
            name='CommodityScrapeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('code_no', models.CharField(blank=True, max_length=120, null=True)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrape_events', to='commodities.commodity')),
            ],
        ),
    ]
