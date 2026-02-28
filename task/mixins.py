from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispetch(self, request, *args, **kwargs):
        isinstance = self.get_object()
        if isinstance != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
