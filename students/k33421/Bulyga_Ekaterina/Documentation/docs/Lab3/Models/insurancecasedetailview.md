<h1>Представление для запросов UPDATE и DELETE к таблице InsuranceCase</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице InsuranceCase.</p>
<pre>
<code>
class InsuranceCaseListCreateView(generics.ListCreateAPIView):
    queryset = InsuranceCase.objects.all()
    serializer_class = InsuranceCaseSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>