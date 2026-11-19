from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, sum, count
spark = SparkSession.builder.appName("EmployeeDataManipulation").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
employee_data = [
(101, "Ravi", 45, "Hyderabad", "Telangana", 60000),
(102, "Priya", 62, "Chennai", "Tamil Nadu", 120000),
(103, "Arun", 55, "Bangalore", "Karnataka", 75000),
(104, "Sneha", 65, "Hyderabad", "Telangana", 55000)
]
columns = ["emp_id", "emp_name", "emp_age", "city", "state", "salary"]
employeeDF = spark.createDataFrame(employee_data, columns)
print("Original DataFrame")
employeeDF.show()
print("Filter: salary > 70000")
employeeDF.filter(col("salary") > 70000).show()
print("Sort: salary descending")
employeeDF.orderBy(col("salary").desc()).show()
print("Add column: annual_salary")
addedDF = employeeDF.withColumn("annual_salary", col("salary") * 12)
addedDF.show()
print("Delete column: annual_salary")
addedDF.drop("annual_salary").show()
print("GroupBy state")
employeeDF.groupBy("state").count().show()
print("Aggregations")
employeeDF.groupBy("state").agg(
avg("salary").alias("average_salary"),
max("salary").alias("max_salary"),
min("salary").alias("min_salary"),
sum("salary").alias("total_salary"),
count("emp_id").alias("employee_count")
).show()
spark.stop()
