from users.models import UserSettings

def get_users_settings(user_requested):
    """
    custom function for getting the users settigs fields
    """
    
    user_settings = UserSettings.objects.filter(user=user_requested)
    if user_settings:
        return {
            'username': user_settings.username_option,
            'email': user_settings.email_option,
            'password': user_settings.password_option,
            'paassword2': user_settings.password2_option,
            'first_name': user_settings.first_name_option,
            'last_name': user_settings.last_name_option,
            'mobile_number': user_settings.mobile_number_option,
        }