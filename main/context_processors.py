from main.models import Profile


def user_profile(request):
    user = request.user

    if user.is_authenticated:
        return {"profile": Profile.objects.get(user=user)}
    else:
        return {"profile": None}
