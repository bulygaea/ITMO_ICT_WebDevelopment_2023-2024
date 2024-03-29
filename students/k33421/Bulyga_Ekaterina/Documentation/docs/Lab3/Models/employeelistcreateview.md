<h1>Представление для GET и POST запросов к таблице Employee</h1>
<p>Представление, реализующее http-запросы GET и POST к таблице Employee.</p>
<pre>
<code>
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>