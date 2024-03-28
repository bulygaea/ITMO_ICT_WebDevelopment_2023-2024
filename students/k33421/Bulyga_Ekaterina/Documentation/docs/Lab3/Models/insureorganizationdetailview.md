<h1>Представление для запросов UPDATE и DELETE к таблице InsureOrganization</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице InsureOrganization.</p>
<pre>
<code>
class InsureOrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsureOrganization.objects.all()
    serializer_class = InsureOrganizationSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>