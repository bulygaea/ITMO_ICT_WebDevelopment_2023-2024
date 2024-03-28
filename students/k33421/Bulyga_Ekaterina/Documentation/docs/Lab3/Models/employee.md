<h1>Модель Employee</h1>
<p>Модель Employee представляет собой сотрудника.</p>
<pre>
<code>
class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, default=None)
    age = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Type, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, to_field='code')
</code>
</pre>