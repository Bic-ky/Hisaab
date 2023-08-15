from account.models import User


def detectUser(user):
    if user.role == User.KITCHEN:
        if user.is_verified and user.is_active:
            redirectUrl = 'account:vendordashboard'
        else:
            redirectUrl = 'account:vprofile' if user.is_active else None

    elif user.role == User.WAITER:
        if user.is_verified and user.is_active:
            redirectUrl = 'account:custdashboard'
        else:
            redirectUrl = 'account:cprofile' if user.is_active else None

    elif user.role == User.COUNTER:
        if user.is_verified and user.is_active:
            redirectUrl = 'account:custdashboard'
        else:
            redirectUrl = 'account:cprofile' if user.is_active else None
            
    elif user.role == None and user.is_superuser:
        redirectUrl = '/admin'
        return redirectUrl
    else:
        redirectUrl = None
    
    return redirectUrl