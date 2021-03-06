from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

import django_filters

from core.paginations import SmallPagination
from core.permissions import IsAuthenticated
from .serializer import (
    PartnerDetailsSerializer,
    PartnerProjectSerializer,
    PartnerProjectPatchSerializer,
)
from .models import PartnerProject
from .filters import PartnerProjectFilter


class PartnerDetailsAPIView(RetrieveAPIView):
    """
    Endpoint for getting Partner Details for overview tab.
    """
    serializer_class = PartnerDetailsSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        """
        Get User Partner Details.
        """
        serializer = self.get_serializer(
            request.user.partner
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class PartnerProjectListCreateAPIView(ListCreateAPIView):

    serializer_class = PartnerProjectSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = SmallPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filter_class = PartnerProjectFilter
    lookup_field = lookup_url_kwarg = 'cluster_id'

    def get_queryset(self, *args, **kwargs):
        queryset = PartnerProject.objects.select_related('partner').prefetch_related('clusters', 'locations')
        cluster_id = self.kwargs.get(self.lookup_field)
        if cluster_id:
            return queryset.filter(clusters__in=[cluster_id])
        return queryset.all()

    def add_many_to_many_relations(self, instance):
        """
        Adding other many to many relations that can be posted like clusters and locations.
        :param instance:
        :return: list of errors or False
        """
        errors = []
        try:
            for location in self.request.data['locations']:
                instance.locations.add(int(location['id']))
        except Exception as exp:
            # TODO log
            errors.append({"locations": "list of dict ids fail."})

        try:
            for cluster in self.request.data['clusters']:
                instance.clusters.add(int(cluster['id']))
        except Exception as exp:
            # TODO log
            errors.append({"clusters": "list of dict ids fail."})

        return errors or False

    def post(self, request, *args, **kwargs):
        """
        Create on PartnerProject model
        :return: PartnerProject object id
        """
        serializer = self.get_serializer(data=self.request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        errors = self.add_many_to_many_relations(serializer.instance)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'id': serializer.instance.id}, status=status.HTTP_201_CREATED)


class PartnerProjectAPIView(APIView):
    """
    PartnerProject CRUD endpoint
    """
    permission_classes = (IsAuthenticated, )

    def get_instance(self, request, pk=None):
        try:
            instance = PartnerProject.objects.get(id=(pk or request.data['id']))
        except PartnerProject.DoesNotExist:
            # TODO: log exception
            raise Http404
        return instance

    def get(self, request, pk, *args, **kwargs):
        instance = self.get_instance(request, pk)
        serializer = PartnerProjectSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        serializer = PartnerProjectPatchSerializer(
            instance=self.get_instance(self.request, pk),
            data=self.request.data
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_instance(request, pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
