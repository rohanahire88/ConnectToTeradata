
# coding: utf-8

# In[11]:


import teradata
import re	

#Below statement helps establish queryband, so that we can identify the performance stats for this session in dbql
udaExec = teradata.UdaExec (appName="ConnectToTeradata", version="1.0",logConsole=False)

#This creates the connection string
session = udaExec.connect(method="odbc", system="tdbatchcop1.intra.searshc.com", username="rahire", password="Welcome99");

#Define empty list
list = []

#Select sample 10 rows for two columns from table and store the data in a list
#The session.execute method can execute all queries
for row in session.execute("SELECT top 10 databasename,tablename FROM dbc.tablesv", queryTimeout=60):
	list.append([getattr(row,'tablename')])


# In[12]:


print list


# In[31]:


from google.cloud import bigquery

client = bigquery.Client.from_service_account_json("H:\\2018\\teradata\syw-analytics-repo-prod-0874ee00257b.json")

# print "H:\\2018\\teradata\syw-analytics-repo-prod-0874ee00257b.json"

GOOGLE_APPLICATION_CREDENTIALS='H:\2018\teradata\syw-analytics-repo-prod-0874ee00257b.json'

query_job = client.query("""
    select tbl_nm from
    `syw-analytics-repo-prod.audit_log.gcp_bq_tracker` limit 1""")

results = query_job.result()  # Waits for job to complete.
print type(results)

