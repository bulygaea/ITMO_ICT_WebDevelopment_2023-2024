<h1>Представление для GET и POST запросов к таблице InsureOrganization</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице InsureOrganization.</p>
<pre>
<code>
class InsureOrganizationListCreateView(generics.ListCreateAPIView):
    queryset = InsureOrganization.objects.all()
    serializer_class = InsureOrganizationSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>