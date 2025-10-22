docker run -d -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 --name sql_server -v mysql_data:/var/lib/mysql  mysql:8.0.20
#docker启动命令