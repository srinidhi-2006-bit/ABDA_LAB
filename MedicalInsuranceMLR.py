from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
spark = SparkSession.builder.appName("MedicalInsuranceMLR").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("Q10_medical_insurance.csv", header=True, inferSchema=True)
assembler = VectorAssembler(
inputCols=["age", "bmi", "children"],
outputCol="features"
)
df = assembler.transform(df)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
lr = LinearRegression(featuresCol="features", labelCol="charges")
model = lr.fit(train_data)
print("Model Parameters:")
print("Intercept:", model.intercept)
print("Coefficients:", model.coefficients)
predictions = model.transform(test_data)
print("Predictions:")
predictions.select("age", "bmi", "children", "charges", "prediction").show()
evaluation = model.evaluate(test_data)
print("Model Evaluation:")
print("RMSE:", evaluation.rootMeanSquaredError)
print("R2:", evaluation.r2)
spark.stop()
