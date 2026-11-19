object EmployeeSequenceOperations {
def main(args: Array[String]): Unit = {
val salaries = Seq(60000, 120000, 75000, 55000)
println("Original sequence: " + salaries)
println("Element at index 2: " + salaries(2))
println("Reverse: " + salaries.reverse)
println("Index of 75000: " + salaries.indexOf(75000))
println("Starts with 60000? " + salaries.startsWith(Seq(60000)))
println("Ends with 55000? " + salaries.endsWith(Seq(55000)))
println("Patch: " + salaries.patch(1, Seq(80000), 1))
println("Max: " + salaries.max)
println("Filter (>80000): " + salaries.filter(_ > 80000))
println("Reduce(sum): " + salaries.reduce(_ + _))
println("Length: " + salaries.length)
println("Head: " + salaries.head)
println("Tail: " + salaries.tail)
println("Contains 75000? " + salaries.contains(75000))
}
}