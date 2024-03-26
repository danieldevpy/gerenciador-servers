

class RequestCommands:

    @classmethod
    def get_previous_url(cls, request):
        if 'HTTP_REFERER' in request.META:
            return request.META['HTTP_REFERER']
        else:
            False
        
    