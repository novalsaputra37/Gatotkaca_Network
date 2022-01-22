from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class ProjectModel(models.Model):
    judul       = models.CharField(max_length=255)
    isi         = models.TextField()
    cover       = models.ImageField(upload_to='content/cover')
    gambar1     = models.ImageField(upload_to='content/gambar1', blank=True)
    gambar2     = models.ImageField(upload_to='content/gambar2', blank=True)
    gambar3     = models.ImageField(upload_to='content/gambar3', blank=True)

    KATAGORI_CHOICES = [
    ('Networking', 'Networking'),
    ('Design', 'Design'),
    ('Dekstop App', 'Dekstop App'),
    ('Mobile App', 'Mobile App'),
    ('Website', 'Website'),
    ('Architect', 'Architect'),
    ]

    kategori    = models.CharField(max_length=50, choices=KATAGORI_CHOICES)
    published   = models.DateTimeField(auto_now_add=True)
    updated 	= models.DateTimeField(auto_now=True)
    slug		= models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()
    
    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('project:detail', kwargs = url_slug)
    
    def __str__(self):
        return "{}. {}".format(self.id, self.judul)