# PySpark Partition Assignment

## Tasks

- Generate 5 million records using spark.range()
- Display initial partitions
- Repartition to 12 partitions
- Coalesce to 3 partitions

## Build

docker build -t partition-app .

## Run

docker run partition-app