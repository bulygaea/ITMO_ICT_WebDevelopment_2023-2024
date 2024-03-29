<h1>Модель InsureOrganization</h1>
<p>Модель InsureOrganization представляет собой страховую организацию.</p>
<pre>
<code>
class InsureOrganization(models.Model):
    fullname = models.CharField(max_length=255)
    shortname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
</code>
</pre>