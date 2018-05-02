import teradata
import re	

#Below statement helps establish queryband, so that we can identify the performance stats for this session in dbql
udaExec = teradata.UdaExec (appName="ConnectToTeradata", version="1.0",logConsole=False)

#This creates the connection string
session = udaExec.connect(method="odbc", system="servername",
username="xxxxx", password="xxxxx");

#Select sample 10 rows for two columns from table and store the data in a list
#The session.execute method can execute all queries
for row in session.execute("SELECT top 10 id,name FROM dbname.tablename", queryTimeout=60):
	list.append([getattr(row,'custianid'),getattr(row,'lyltycardnbr')])

#Print show table output on screen
rows = session.execute("SHOW TABLE dbname.tablename")
for row in rows:
	for line in re.split("\r\n|\n\r|\r|\n", row[0]):
		print(line)