<h1>Представление для запросов UPDATE и DELETE к таблице Individual</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице Individual.</p>
<pre>
<code>
class IndividualDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>