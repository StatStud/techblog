---
title: "Db Pulls in R"
date: 2023-10-23T09:19:42-07:00
draft: false
tags: ['R','Data-Engineering']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

Below is a sequential way of batching data by year and ingesting as a set of csv files from a SQL server.

```r

install.packages("data.table")
install.packages("RODBC")
library(data.table)
library(RODBC)

cxn <- odbcDriverConnect('Driver={ODBC DRIVER 13 for SQL Server};Server=website.com;Trusted_Connection=yes')

file_base = "base/dir/folder/for/data"
table_name <- "schema.table_a"
date_column <- "date_col"
for (year in 1950:2020){
    print(paste("starting year", year))
    start_date <- paste0(year,'-01-01')
    end_date <- paste0(year,'-12-31')
    query <- sprintf("select * from %s where %s between %s and %s",
                        table_name, date_column,
                        start_date, end_date)
    df <- sqlQuery(cxn,query)
    df = data.table(df)
    file_name <- paste0("suffix_",year,".csv")
    write.table(df,file-file.path(file_base,file_name), 
                                    row.names=FALSE, sep = "|",
                                    col.names=TRUE)
}

```

To run your R script from the command line, simply run:

```sh
R CMD BATCH script.R
```