<h1>Представление для GET и POST запросов к таблице Individual</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице Individual.</p>
<p>В дальнейшем понадобится отображать имена и фамилии людей, а также получать по ним их id, поэтому реализована фильтрация с помощью GET-запроса.</p>
<pre>
<code>
class IndividualListCreateView(generics.ListCreateAPIView):
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Individual.objects.all()
        firstname = self.request.query_params.get('firstname')
        if firstname:
            queryset = queryset.filter(firstname=firstname)
        lastname = self.request.query_params.get('lastname')
        if lastname:
            queryset = queryset.filter(lastname=lastname)
        return queryset
</code>
</pre>