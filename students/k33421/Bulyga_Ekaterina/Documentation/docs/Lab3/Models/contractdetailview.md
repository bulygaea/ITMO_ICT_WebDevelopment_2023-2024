<h1>Представление для запросов UPDATE и DELETE к таблице Contract</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице Contract.</p>
<pre>
<code>
class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>