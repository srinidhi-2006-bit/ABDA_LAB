import scala.io.StdIn.readInt
class InsufficientBalanceException(msg: String) extends Exception(msg)
class BankAccount(
val accNo: Int,
var name: String,
var balance: Double
) {
def deposit(amount: Double): Unit = {
if (amount <= 0)
throw new IllegalArgumentException("Amount must be positive")
balance += amount
println("Amount Deposited successfully")
}
def withdraw(amount: Double): Unit = {
if (amount <= 0)
throw new IllegalArgumentException("Amount must be positive")
else if (amount > balance)
throw new InsufficientBalanceException("Insufficient Balance")
else {
balance -= amount
println("Withdrawal successful")
}
}
def displayBalance(): Unit = {
println("Current Balance = " + balance)
}
}
object BankSystem {
def main(args: Array[String]): Unit = {
val account = new BankAccount(101, "Srinidhi", 5000)
var choice = 0
while (choice != 4) {
println("------ BANK MENU ------")
println("1. Deposit")
println("2. Withdraw")
println("3. Display Balance")
println("4. Exit")
print("Enter choice: ")
choice = readInt()
try {
choice match {
case 1 =>
print("Enter Deposit Amount: ")
val amount = readInt()
account.deposit(amount)
case 2 =>
print("Enter Withdrawal Amount: ")
val amount = readInt()
account.withdraw(amount)
case 3 =>
account.displayBalance()
case 4 =>
println("Thank you")
case _ =>
println("Invalid choice")
}
} catch {
case e: InsufficientBalanceException =>
println("Exception : " + e.getMessage)
case e: IllegalArgumentException =>
println("Exception : " + e.getMessage)
} finally {
println("Transaction Completed")
}
}
}
}