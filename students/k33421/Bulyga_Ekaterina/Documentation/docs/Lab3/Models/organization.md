<h1>Модель Organization</h1>
<p>Модель Organization представляет собой юридическое лицо (организацию).</p>
<pre>
<code>
class Organization(models.Model):
    types = (
        ('медицинское учреждение', 'медицинское учреждение'),
        ('автотранспортное предприятие', 'автотранспортное предприятие'),
        ('учебное заведение', 'учебное заведение'),
        ('другое', 'другое')
    )
    code = models.PositiveIntegerField(primary_key=True)
    fullname = models.CharField(max_length=255)
    shortname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bank_number = models.PositiveBigIntegerField()
    type = models.CharField(max_length=35, choices=types)
</code>
</pre>