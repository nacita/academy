from django.conf import settings

from academy.apps.accounts.models import User


def user_profile(user: User) -> dict:
    user_data = {
        'name': user.name,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'is_active': user.is_active,
        'avatar': "",
        'linkedin': "",
        'git_repo': "",
        'blog': "",
        'facebook': "",
        'youtube': "",
        'twitter': "",
        'instagram': "",
        'telegram_id': "",
        'curriculum_vitae': "",
        'has_profile': False
    }

    if hasattr(user, 'profile'):
        profile = user.profile
        avatar = settings.MEDIA_HOST + profile.avatar.url \
            if profile.avatar else None
        cv = settings.MEDIA_HOST + profile.curriculum_vitae.url \
            if user.profile.curriculum_vitae else None

        user_data['has_profile'] = True
        user_data['avatar'] = avatar
        user_data['linkedin'] = profile.linkedin
        user_data['git_repo'] = profile.git_repo
        user_data['blog'] = profile.blog
        user_data['facebook'] = profile.facebook
        user_data['facebook'] = profile.facebook
        user_data['youtube'] = profile.youtube
        user_data['youtube'] = profile.youtube
        user_data['twitter'] = profile.twitter
        user_data['instagram'] = profile.instagram
        user_data['telegram_id'] = profile.telegram_id
        user_data['telegram_id'] = profile.telegram_id
        user_data['curriculum_vitae'] = cv

    return user_data


def logo(logo):
    """
    this serializer for LogoPerner and LogoSponsor
    """
    return {
        'name': logo.name,
        'image': settings.MEDIA_HOST + logo.image.url,
        'display_order': logo.display_order,
        'website': logo.website
    }