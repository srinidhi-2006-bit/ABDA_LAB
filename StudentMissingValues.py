from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("StudentMissingValues").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
data = [
(101, "Ravi", "CSE", "Male", 85),
(102, "Priya", None, "Female", None),
(103, "Arun", "CSE", "Male", 78),
(104, "Sneha", None, "Female", 92)
]
columns = ["student_id", "student_name", "department", "gender", "marks"]
studentDF = spark.createDataFrame(data, columns)
print("Original DataFrame")
studentDF.show()
print("Missing value count")
for column_name in studentDF.columns:
    missing_count = studentDF.filter(col(column_name).isNull()).count()
    print(column_name, ":", missing_count)
print("Data after replacing missing values")
cleanedDF = studentDF.fillna({"marks": 0, "department": "Unknown"})
cleanedDF.show()
spark.stop()
