<h1>Модель Individual</h1>
<p>Модель Individual представляет собой физическое лицо.</p>
<pre>
<code>
class Individual(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, default=None)
    passport = models.PositiveBigIntegerField()
    phone = models.PositiveBigIntegerField()
    address = models.CharField(max_length=255)
</code>
</pre>