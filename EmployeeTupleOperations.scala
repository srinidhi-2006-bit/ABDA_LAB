object EmployeeTupleOperations {
def main(args: Array[String]): Unit = {
val employee = (101, "Ravi", 60000.0)
println("Tuple: " + employee)
println("First: " + employee._1)
println("Second: " + employee._2)
println("Third: " + employee._3)
val copiedTuple = employee
println("Copied Tuple: " + copiedTuple)
println("Tuple elements:")
employee.productIterator.foreach(println)
println("Tuple as List: " + employee.productIterator.toList)
println("Tuple size: " + employee.productArity)
println("Tuple as String: " + employee.toString)
val swapped = (employee._2, employee._1, employee._3)
println("Tuple swapped: " + swapped)
}
}