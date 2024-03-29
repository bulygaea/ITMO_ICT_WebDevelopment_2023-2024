<h1>Представление для запросов UPDATE и DELETE к таблице InsureAgent</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице InsureAgent.</p>
<pre>
<code>
class InsureAgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsureAgent.objects.all()
    serializer_class = InsureAgentSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>