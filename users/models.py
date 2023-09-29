from django.db import models
from django.contrib.auth.models import User

countries = [
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AG', 'Antigua and Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Republic'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CD', 'Congo, Democratic Republic of the'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote d\'Ivoire'),
]


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=24, choices=countries, blank=False, null=False)
    street_address = models.CharField(max_length=24, blank=False, null=False)
    street_address_detail = models.CharField(max_length=9, blank=True, null=True)
    postcode = models.IntegerField(blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    additional_info = models.TextField(blank=True, null=True)
