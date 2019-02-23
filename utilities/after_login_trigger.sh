me=$(whoami)


if [ -n "$SSH_CLIENT" ]; then
    curl -H "Content-Type: application/json" -X POST -d '{"user_name": "'${me}'", "login_type": "ssh"}' http://localhost:5000/notify_login/
else
    curl -H "Content-Type: application/json" -X POST -d '{"user_name": "'${me}'", "login_type": "local"}' http://localhost:5000/notify_login/
fi
