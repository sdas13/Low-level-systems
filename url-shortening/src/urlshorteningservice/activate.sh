# ./venv/bin/python3 run.py
source ./venv/bin/activate
# export "FLASK_APP=run:init_app()"
# flask run --port $1
ulimit -n 2048
gunicorn --workers 4 --worker-class eventlet --threads 2 -b 0.0.0.0:5000 --access-logfile log.log --error-logfile error.log --capture-output "run:init_app()"
