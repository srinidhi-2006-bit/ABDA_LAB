object CricketTracker {
def main(args: Array[String]): Unit = {
var players = Map(
"Virat" -> 45,
"Rohit" -> 30,
"Gill" -> 55,
"Hardik" -> 20
)
println("Initial scoreboard")
println(players)
players += ("KL Rahul" -> 10)
println("After adding KL Rahul")
println(players)
players += ("Virat" -> 60)
println("After updating Virat's score")
println(players)
println("Virat's runs: " + players.getOrElse("Virat", "Player Not found"))
println("Dhoni's runs: " + players.getOrElse("Dhoni", "Player Not found"))
players -= "Hardik"
println("After Hardik retires")
println(players)
println("Players with 50+ runs")
players.filter(_._2 >= 50).foreach(println)
println("Total Active Players: " + players.size)
println("Players: " + players.keySet)
println("Runs: " + players.values)
println("Is Rohit playing? " + players.contains("Rohit"))
}
}