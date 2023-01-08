#!/bin/bash
mysql -h $DB_SERVER -uroot -pstudent /home/init_database.sh
mysql -h $DB_SERVER -uroot -pstudent $DB_NAME /home/database_dump.sh
mysql -h $DB_SERVER -uroot -pstudent $DB_NAME /home/presta_db_config.sh