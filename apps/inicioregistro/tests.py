from config.wsgi import *
from django.contrib.auth.models import User
#para que funcione el test con los archivos del .env, debe ejecutarse el load_dotenv al inicio del settings

user=User.objects.filter(username='daniel')
if user:
    print('existe')
else:
    print('no existe')
