from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

class AdminRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_admin:
            return redirect(reverse_lazy('home'))
        response = super().dispatch(request, *args, **kwargs)

        if hasattr(response, 'render') and callable(response.render):
            response.render()
        return response
    
class UserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)
        