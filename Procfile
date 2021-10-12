release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
release: python3 manage.py makemigrations authenticationApp
release: python3 manage.py migrate --no-input
release: python3 manage.py makemigrations ireporterApp
release: python3 manage.py migrate --no-input
web: gunicorn ireporterManager.wsgi