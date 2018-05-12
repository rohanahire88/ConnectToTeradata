package main

import (
"log"
"database/sql"
"fmt"
_ "github.com/alexbrainman/odbc"
)

func main() {

/*Connection String*/
db, err := sql.Open("odbc", "DSN=connect_td")
if err != nil {
        fmt.Println("Could not connect to db:", err)
}

err = db.Ping()
if err != nil {
        fmt.Println("got an error:", err)
}

fmt.Println("Connection successful")

/* Define Variables*/
var (
	databasename string
	tablename string
)

/*Selecting 2 columns from table*/
rows, err := db.Query("select top 10 databasename,tablename from dbc.tables")
if err != nil {
	log.Fatal(err)
}

/*assign results to variables, a row at a time, with rows.Scan()*/
defer rows.Close()
for rows.Next() {
	err := rows.Scan(&databasename, &tablename)
	if err != nil {
		log.Fatal(err)
	}
	log.Println(databasename, tablename)
}
err = rows.Err()
if err != nil {
	log.Fatal(err)
}

}



