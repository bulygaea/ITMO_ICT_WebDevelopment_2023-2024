<h1>Представление для GET и POST запросов к таблице Type</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице Type.</p>
<pre>
<code>
class TypeListCreateView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>