from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    subdomain_prefix = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="organizations/logos")

    account_name_alias = models.CharField(
        max_length=40, blank=True, help_text="Used on signup screen, typically specifies what the funding is for")
    student_account_alias = models.CharField(
        max_length=40, blank=True, help_text="used in signup screens. should be prefixed with the appropriate a/an")
    whatsapp_contact = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    instagram = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name


class OrganizationAwareModel(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_organization")

    class Meta:
        abstract = True


class Carousel(models.Model):
    organization = models.ForeignKey(
        Organization, blank=False, null=False, on_delete=models.CASCADE, related_name="carousels")
    image = models.ImageField(upload_to="organizations/carousels")
    header = models.CharField(max_length=200)
    body = models.CharField(max_length=300)

    def __str__(self):
        return self.header

class Asset(models.Model):
    organization = models.OneToOneField(Organization, blank=False, null=False, on_delete=models.CASCADE, related_name="asset")
    about_image = models.ImageField(upload_to="organizations/assets", blank=True, null=True)
    about_image_2 = models.ImageField(upload_to="organizations/assets", blank=True, null=True)

    def __str__(self):
        return self.organization.name
