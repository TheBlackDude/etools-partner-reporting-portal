from rest_framework import serializers

from cluster.serializers import ClusterSimpleSerializer
from core.serializers import ShortLocationSerializer
from core.common import PD_STATUS
from .models import (
    Partner,
    PartnerProject,
)


class PartnerDetailsSerializer(serializers.ModelSerializer):

    partner_type_long = serializers.CharField(source='get_partner_type_display')
    shared_partner_long = serializers.CharField(source='get_shared_partner_display')

    class Meta:
        model = Partner
        fields = (
            # Partner Details part
            'id',
            'title',
            'short_title',
            'alternate_title',
            'vendor_number',
            'partner_type',
            'partner_type_long',
            'shared_partner_long',
            'shared_partner',
            'core_values_assessment_date',
            'address',
            'street_address',
            'city',
            'postal_code',
            'country',
            'country_code',
            'email',
            'phone_number',
            # Risk Rating part
            'last_assessment_date',
            'type_of_assessment',
            'rating'
        )


class PartnerProjectSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    clusters = ClusterSimpleSerializer(many=True, read_only=True)
    locations = ShortLocationSerializer(many=True, read_only=True)
    partner = serializers.SerializerMethodField()

    class Meta:
        model = PartnerProject
        fields = (
            'id',
            'title',
            'start_date',
            'end_date',
            'status',
            'description',
            'additional_information',
            'total_budget',
            'funding_source',
            'clusters',
            'locations',
            'partner',
            # 'reportables',
        )

    def get_id(self, obj):
        return str(obj.id)

    def get_partner(self, obj):
        return obj.partner and str(obj.partner_id)


class PartnerProjectPatchSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    status = serializers.ChoiceField(choices=PD_STATUS, required=False)
    description = serializers.CharField(required=False)
    additional_information = serializers.CharField(required=False)
    total_budget = serializers.CharField(required=False)
    funding_source = serializers.CharField(required=False)
    clusters = serializers.CharField(required=False)
    locations = serializers.CharField(required=False)
    partner = serializers.CharField(required=False)

    class Meta:
        model = PartnerProject
        fields = (
            'id',
            'title',
            'start_date',
            'end_date',
            'status',
            'description',
            'additional_information',
            'total_budget',
            'funding_source',
            'clusters',
            'locations',
            'partner',
            # 'reportables',
        )
