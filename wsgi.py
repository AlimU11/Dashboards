from app import app
from app import app as application

application = app.server

# for local
# waitress-serve --host=127.0.0.1 --port=8050 wsgi:application
