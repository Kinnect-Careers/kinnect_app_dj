release: pip freeze
release: python src/manage.py migrate
web: gunicorn config.wsgi --chdir src --log-file -
