from rest_framework.serializers import HyperlinkedModelSerializer
from accounts.serializers import UserSerializer
from redflag.models import Redflag
class RedflagSerializer(HyperlinkedModelSerializer):
    redflag_createdby = UserSerializer(read_only=True)

    class Meta:
        model = Redflag
        fields = ('redflag_title', 'redflag_comment', 'redflag_date', 'redflag_status',
                  'redflag_image', 'redflag_video', 'redflag_createdby', 'redflag_location')
