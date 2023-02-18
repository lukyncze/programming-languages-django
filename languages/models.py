from django.db import models
from django.urls import reverse

class Typ(models.Model):
    oznaceni_typu = models.CharField(max_length=50, unique=True, verbose_name="Označení typu jazyku",
                            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    DRUH = (
        ('vyšší', 'vyšší programovací jazyk'),
        ('nižší', 'nižší programovací jazyk'),
    )
    druh = models.CharField(max_length=20, choices=DRUH, blank=True, default='vyšší', verbose_name="Druh", help_text='Vyberte označení druhu programovacího jazyku')

    class Meta:
        ordering = ["oznaceni_typu"]
        verbose_name = 'Typ jazyku'
        verbose_name_plural = 'Typy jazyku'

    def __str__(self):
        return f"{self.oznaceni_typu}, {self.druh}"

class Jazyk(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název jazyku", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis jazyku")
    OBLIBENOST = (
        (5, 'naprosto oblíbený'),
        (4, 'oblíbený'),
        (3, 'průměr'),
        (2, 'neoblíbený'),
        (1, 'ten se ani neuč'),
    )
    oblibenost = models.IntegerField(choices=OBLIBENOST, blank=True, default=3, verbose_name="Oblíbenost jazyku", help_text='Vyberte oblíbenost jazyku')
    foto = models.ImageField(upload_to='jazyky/%Y/%m/%d/', blank=True, null=True, verbose_name="Logo jazyku")
    typ = models.ForeignKey(Typ, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Jazyk'
        verbose_name_plural = 'Jazyky'

    def __str__(self):
        return f"{self.nazev}, {self.oblibenost}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
