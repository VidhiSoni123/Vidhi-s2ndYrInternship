# PySpark Employee Processing

## Features

- Sort employees by salary in descending order
- Calculate department-wise salary totals
- Save top 3 highest-paid employees to a file

## Build Docker Image

docker build -t pyspark-employee .

## Run Container

docker run pyspark-employee

## Output File

output/top3_employees.txt