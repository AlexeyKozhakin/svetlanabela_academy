from main.models import Profile


def user_profile(request):
    user = request.user
    profile_context = {"profile": None}  # Users with no profile ie superuser
    if user.is_authenticated:
        try:
            profile_context["profile"] = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            pass
    return profile_context
