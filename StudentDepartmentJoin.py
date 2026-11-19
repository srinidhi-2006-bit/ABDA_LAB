from pyspark.sql import SparkSession
spark = SparkSession.builder \
.appName("StudentDepartmentJoin") \
.master("local[*]") \
.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
student_data = [
(101, "Ravi", "CSE", "Male", 85),
(102, "Priya", "ECE", "Female", 90),
(103, "Arun", "CSE", "Male", 78),
(104, "Sneha", "MECH", "Female", 92)
]
student_columns = [
"student_id", "student_name", "department_id", "gender", "marks"
]
studentDF = spark.createDataFrame(student_data, student_columns)
department_data = [
("CSE", "Computer Science"),
("ECE", "Electronics"),
("EEE", "Electrical"),
("MECH", "Mechanical")
]
department_columns = ["department_id", "department_name"]
deptDF = spark.createDataFrame(department_data, department_columns)
print("Student DataFrame")
studentDF.show()
print("Department DataFrame")
deptDF.show()
print("Inner Join")
studentDF.join(
deptDF, "department_id", "inner"
).show()
print("Left Semi Join")
studentDF.join(
deptDF, "department_id", "left_semi"
).show()
print("Outer Join")
studentDF.join(
deptDF, "department_id", "outer"
).show()
spark.stop()