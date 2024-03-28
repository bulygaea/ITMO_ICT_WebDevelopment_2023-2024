<h1>Представление для GET и POST запросов к таблице Organization</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице Organization.</p>
<p>В дальнейшем понадобится отображать полное наименование организации, а также получать по нему ее id, поэтому реализована фильтрация с помощью GET-запроса.</p>
<pre>
<code>
class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Organization.objects.all()
        fullname = self.request.query_params.get('fullname')
        if fullname:
            queryset = queryset.filter(fullname=fullname)
        return queryset
</code>
</pre>