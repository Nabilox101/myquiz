from django.db import models

class EnglishToDarija(models.Model):
    NOUNF = 'noun femn'
    NOUNM = 'noun masc'
    VERB = 'verb'
    ADJECTIVE = 'adjective'
    ADVERB = 'adverb'
    SINGULAR = 'singular'
    PLURAL = 'plural'
    NEUTRAL = ':'
    PART_OF_SPEECH_CHOICES = [
        (NOUNF, 'Noun Femn'),
        (NOUNM, 'Noun Masc'),
        (VERB, 'Verb'),
        (ADJECTIVE, 'Adjective'),
        (ADVERB, 'Adverb'),
    ]
    PLURALITY_CHOICES = [
        (NEUTRAL, ':'),
        (SINGULAR, 'Singular'),
        (PLURAL, 'Plural'),
    ]

    english_word = models.CharField(max_length=100)
    darija_translation = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=20,
        choices=PART_OF_SPEECH_CHOICES,
        default=NOUNF,
    )
    plurality = models.CharField(
        max_length=20,
        choices=PLURALITY_CHOICES,
        default=NEUTRAL,
    )
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    audio = models.FileField(upload_to='audio', null=True, blank=True)

    def __str__(self):
        return f"{self.english_word} ({self.get_part_of_speech_display()}) ({self.get_plurality_display()}) : {self.darija_translation}"

class Example(models.Model):
    english_to_darija = models.ForeignKey(EnglishToDarija, on_delete=models.CASCADE)
    example_text = models.TextField()

    def __str__(self):
        return self.example_text
