object StudentSetOperations {
def main(args: Array[String]): Unit = {
var students = Set("Ravi", "Priya", "Arun", "Sneha")
println("Original set: " + students)
students += "Kiran"
println("After adding: " + students)
students -= "Priya"
println("After removing: " + students)
println("Contains Ravi: " + students.contains("Ravi"))
println("Size: " + students.size)
val otherSet = Set("Ravi", "Arun", "Manoj")
println("Union: " + (students union otherSet))
println("Intersection: " + (students intersect otherSet))
println("Difference: " + (students diff otherSet))
}
}