#mysqldump -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  > db-backup.sql
cd ../../backups
mysqldump -u imonje -h imonje.mysql.pythonanywhere-services.com 'imonje$air'  > "$(date +%F_%R)".sql

#mysql -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  < db-backup.sql

