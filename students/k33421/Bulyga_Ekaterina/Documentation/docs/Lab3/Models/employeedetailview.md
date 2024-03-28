<h1>Представление для запросов UPDATE и DELETE к таблице Employee</h1>
<p>Представление, реализующее http-запросы UPDATE и DELETE к таблице Employee.</p>
<pre>
<code>
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
</code>
</pre>