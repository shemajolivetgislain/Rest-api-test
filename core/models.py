from django.db import models
from django.template.defaultfilters import slugify, truncatewords
from django.urls import reverse


def uploadToMedia(instance, filename):
    """SELECT A POSITION TO STORE ALL PROFILE IMAGES"""
    return 'static/images/{filename}'.format(filename=filename)


recordStatus = (
    ('pending', 'Pending'),
    ('rejected', 'Rejected'),
    ('approved', 'Approved'),
)


class Species(models.Model):
    specie_name = models.CharField(max_length=200, help_text="Use Scientific Name", blank=True, null=True,
                                   verbose_name='Specie Name')
    kinyarwanda_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Kinyarwanda Name')
    sampling_method = models.CharField(max_length=200, blank=False, null=False,
                                       verbose_name='Sampling Method')
    sampling_date = models.DateTimeField(auto_now_add=True,verbose_name='Sampling Date')
    site_description = models.TextField(help_text="Describe site including location name", blank=True, null=True)
    latitude = models.FloatField(blank=False, null=True)
    longitude = models.FloatField(blank=False, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Project Name',
                                    help_text="Tell us in short the project that you are currently working on if any.")
    author = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, choices=recordStatus, blank=True, default='pending')
    thumbnail = models.ImageField(null=True, blank=False, upload_to=uploadToMedia)


    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url

    @property
    def short_comment(self):
        return truncatewords(self.comment, 3)

    @property
    def short_description(self):
        return truncatewords(self.site_description, 3)


    def get_absolute_url(self):
        return reverse('clean_specie', args=[self.slug])


    def __str__(self):
        return self.collector_name.full_name()


