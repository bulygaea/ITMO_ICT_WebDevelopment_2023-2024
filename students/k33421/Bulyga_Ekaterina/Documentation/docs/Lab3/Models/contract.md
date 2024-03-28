<h1>Модель Contract</h1>
<p>Модель Contract представляет собой договор.</p>
<pre>
<code>
class Contract(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    organization = models.ForeignKey(Organization, null=True, on_delete=models.CASCADE, default=None)
    client = models.ForeignKey(Individual, null=True, on_delete=models.CASCADE, default=None)
    agent = models.ForeignKey(InsureAgent, on_delete=models.CASCADE)
</code>
</pre>