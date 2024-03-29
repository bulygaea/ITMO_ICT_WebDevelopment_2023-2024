<h1>Модель InsureAgent</h1>
<p>Модель InsureAgent представляет собой страхового агента.</p>
<pre>
<code>
class InsureAgent(User):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    passport = models.PositiveBigIntegerField()
    phone = models.PositiveBigIntegerField()
    address = models.CharField(max_length=255)
    insureorganization = models.ForeignKey(InsureOrganization, on_delete=models.CASCADE)
</code>
</pre>