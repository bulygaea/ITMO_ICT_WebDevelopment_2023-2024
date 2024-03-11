from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *


class IndividualListCreateView(generics.ListCreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]


class IndividualDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]


class TypeListCreateView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]


class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class InsureOrganizationListCreateView(generics.ListCreateAPIView):
    queryset = InsureOrganization.objects.all()
    serializer_class = InsureOrganizationSerializer
    permission_classes = [IsAuthenticated]


class InsureOrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsureOrganization.objects.all()
    serializer_class = InsureOrganizationSerializer
    permission_classes = [IsAuthenticated]


class InsureAgentListCreateView(generics.ListCreateAPIView):
    queryset = InsureAgent.objects.all()
    serializer_class = InsureAgentSerializer
    permission_classes = [IsAuthenticated]


class InsureAgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsureAgent.objects.all()
    serializer_class = InsureAgentSerializer
    permission_classes = [IsAuthenticated]


class ContractListCreateView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]


class InsuranceCaseListCreateView(generics.ListCreateAPIView):
    queryset = InsuranceCase.objects.all()
    serializer_class = InsuranceCaseSerializer
    permission_classes = [IsAuthenticated]


class InsuranceCaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsuranceCase.objects.all()
    serializer_class = InsuranceCaseSerializer
    permission_classes = [IsAuthenticated]
