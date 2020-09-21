#/usr/bin/env sh

PG_DB=jobs_dashboard
PG_PASSWORD=`head -c 18 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9' | head -c 12`
PG_SERVICE_NAME=postgres
PG_USER=jobs_dashboard_user
PRIVATE_IP=$PRIVATE_IP
PUBLIC_IP=$PUBLIC_IP

echo "POSTGRES_DB=$PG_DB
POSTGRES_PASSWORD=$PG_PASSWORD
POSTGRES_USER=$PG_USER
DATABASE_URL=postgres://$PG_USER:$PG_PASSWORD@$PG_SERVICE_NAME:5432/$PG_DB
SECRET_KEY=`head -c 75 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9' | head -c 50`
PUBLIC_IP=$PUBLIC_IP
PRIVATE_IP=$PRIVATE_IP" > .docker-env
