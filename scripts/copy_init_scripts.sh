#!/bin/bash
SERVICE_NAME=$1

docker cp ../mysql/init_database.sql $SERVICE_NAME:/home/init_database.sql
docker cp ../mysql/init_database.sql $SERVICE_NAME:/home/database_dump.sql
docker cp ../mysql/init_database.sql $SERVICE_NAME:/home/presta_db_config.sql
docker cp ../mysql/init_database.sql $SERVICE_NAME:/home/init_databse.sh

docker container exec $SERVICE_NAME chmod +x /home/init_database.sh
docker container exec $SERVICE_NAME /home/init_database.sh
docker container exec $SERVICE_NAME rm /home/init_database.sh
docker container exec $SERVICE_NAME rm /home/database_dump.sh
docker container exec $SERVICE_NAME rm /home/presta_db_config.sh