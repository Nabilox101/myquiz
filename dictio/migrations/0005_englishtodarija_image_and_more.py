# Generated by Django 4.1.7 on 2023-03-26 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictio', '0004_englishtodarija_part_of_speech'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishtodarija',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='englishtodarija',
            name='part_of_speech',
            field=models.CharField(choices=[('noun femn', 'Noun Femn'), ('noun masc', 'Noun Masc'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('adverb', 'Adverb')], default='noun femn', max_length=20),
        ),
    ]
