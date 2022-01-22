import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote

@endpoints.api(name='echo', version='v1')
class EchoApi(remote.service)

class EchoRequest(messages.Message)
    message = messages.StringField()

class EchoResponse(message.Message):
    """A proto Message that contains a simple string field"""
    message = messages.StringField(1)

ECHO_RESOURCE = endpoints.ResourceContainer(
    EchoRequest,
    n-messages.IntegerField(2, default=1))

@endpoints.method(
    # This method takes  REsourceContainer defined above. 
    ECHO_RESOURCE
    #This method returns an Echo 
    EchoResponse
    path='echo'
    http_methods='POST'
    name='echo')

def echo(self, request):