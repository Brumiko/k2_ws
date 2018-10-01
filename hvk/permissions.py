from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Samo član smije pregledavati i ažurirati svoj profil.
    Zato nema ispitivanja SAFE_METHODS.
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'py_user'):
            return obj.py_user == request.user
        elif hasattr(obj, 'clan'):
            return obj.clan.py_user == request.user
        else:
            raise Exception('Za objekt {0} tipa {1} nisu definirane dozvole.'.format(obj, type(obj)))
