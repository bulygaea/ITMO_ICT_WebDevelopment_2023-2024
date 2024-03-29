<h1>Представление для GET и POST запросов к таблице InsuranceCase</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице InsuranceCase.</p>
<pre>
<code>
class InsuranceCaseListCreateView(generics.ListCreateAPIView):
    queryset = InsuranceCase.objects.all()
    serializer_class = InsuranceCaseSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>