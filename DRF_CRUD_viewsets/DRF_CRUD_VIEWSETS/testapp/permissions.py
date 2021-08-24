from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsReadeonly(BasePermission):
    def has_permissions(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False