from django.db import models
from cloudinary.models import CloudinaryField
from xpro.models import User
# Create your models here.


class Photo(models.Model):
    # Misc Django Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='photo')
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=150, blank=True)

    # Points to a Cloudinary image
    image = CloudinaryField('image')

    """ Informative name for mode """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)