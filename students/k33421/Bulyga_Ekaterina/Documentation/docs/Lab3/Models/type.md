<h1>Модель Type</h1>
<p>Модель Type представляет собой категории сотрудников юр. организации.</p>
<pre>
<code>
class Type(models.Model):
    title = models.CharField(max_length=255)
    summ = models.PositiveSmallIntegerField()
</code>
</pre>