from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault
from accounts.serializers import UserSerializer
from redflag.models import Redflag


class RedflagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Redflag
        fields = ('title', 'comment', 'date', 'status',
                  'image', 'video', 'createdby', 'location')
