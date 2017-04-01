#mysqldump -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  > db-backup.sql
cd /home/imonje/backups
mysqldump -u imonje -h imonje.mysql.pythonanywhere-services.com 'imonje$air'  > db-backup.sql

#mysql -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  < db-backup.sql

