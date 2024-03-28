<h1>Представление для запросов UPDATE и DELETE к таблице Organization</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице Organization.</p>
<pre>
<code>
class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>