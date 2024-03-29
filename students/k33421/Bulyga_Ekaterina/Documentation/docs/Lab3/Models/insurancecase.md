<h1>Модель InsuranceCase</h1>
<p>Модель InsuranceCase представляет собой страховой случай.</p>
<pre>
<code>
class InsuranceCase(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=1023)
    damage_summ = models.PositiveIntegerField()
    payment = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
</code>
</pre>