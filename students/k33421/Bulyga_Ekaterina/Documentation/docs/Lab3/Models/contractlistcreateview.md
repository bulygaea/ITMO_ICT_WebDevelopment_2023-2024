<h1>Представление для GET и POST запросов к таблице Contract</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице Contract.</p>
<p>В дальнейшем понадобится отображать договоры для конкретных страховых агентов, поэтому реализована фильтрация с помощью GET-запроса.</p>
<pre>
<code>
class ContractListCreateView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Contract.objects.all()
        date_from = self.request.query_params.get('date_from')
        if date_from:
            queryset = queryset.filter(date_from=date_from)
        date_to = self.request.query_params.get('date_to')
        if date_to:
            queryset = queryset.filter(date_to=date_to)
        organization = self.request.query_params.get('organization')
        if organization:
            queryset = queryset.filter(organization=organization)
        client = self.request.query_params.get('client')
        if client:
            queryset = queryset.filter(client=client)
        agent = self.request.query_params.get('agent')
        if agent:
            queryset = queryset.filter(agent=agent)
        return queryset
    def post(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
</code>
</pre>