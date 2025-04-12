# filepath: /c:/Users/User 1/.vscode/Django5/mark_registration_system/settings.py
import os

# ...existing code...

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ...existing code...