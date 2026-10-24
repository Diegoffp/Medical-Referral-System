import os 
STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = {
    os.path.join(BASE_DIR, '/static/')
}
MEDIA_ROOT = os.path.join(BASE_DIR, '/static/')
MEDIA_URL = '/media/'
