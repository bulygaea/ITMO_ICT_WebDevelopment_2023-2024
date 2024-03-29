<h1>Представление для запросов UPDATE и DELETE к таблице Type</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице Type.</p>
<pre>
<code>
class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>
