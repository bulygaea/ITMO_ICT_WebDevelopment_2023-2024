<h1>Представление для GET и POST запросов к таблице InsureAgent</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице InsureAgent.</p>
<p>В дальнейшем понадобится отображать логин пользователя, поэтому реализована фильтрация с помощью GET-запроса.</p>
<pre>
<code>
class InsureAgentListCreateView(generics.ListCreateAPIView):
    queryset = InsureAgent.objects.all()
    serializer_class = InsureAgentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = InsureAgent.objects.all()
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)
        return queryset
</code>
</pre>