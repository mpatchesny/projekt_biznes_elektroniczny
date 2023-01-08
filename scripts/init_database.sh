#!/bin/bash
SERVICE_NAME=$1

docker cp ../mysql/database_dump.sh  $SERVICE_NAME:/home/database_dump.sh
docker cp ../mysql/init_database.sql $SERVICE_NAME:/home/init_database.sql
docker cp ../mysql/init_database.sql $SERVICE_NAME:/home/presta_db_config.sql

docker container exec $SERVICE_NAME chmod +x /home/init_database.sh
docker container exec $SERVICE_NAME chmod +x /home/database_dump.sh
docker container exec $SERVICE_NAME chmod +x /home/presta_db_config.sh
docker container exec $SERVICE_NAME mysql -h $DB_SERVER -uroot -pstudent /home/init_database.sh
docker container exec $SERVICE_NAME mysql -h $DB_SERVER -uroot -pstudent $DB_NAME /home/database_dump.sh
docker container exec $SERVICE_NAME mysql -h $DB_SERVER -uroot -pstudent $DB_NAME /home/presta_db_config.sh
docker container exec $SERVICE_NAME rm /home/init_database.sh
docker container exec $SERVICE_NAME rm /home/database_dump.sh