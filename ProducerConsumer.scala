import scala.collection.mutable.Queue
object ProducerConsumer {
val buffer = Queue[Int]()
val size = 5
val producer = new Thread {
override def run(): Unit = {
for (i <- 1 to 10) {
buffer.synchronized {
while (buffer.size == size) {
println("Buffer full, producer waiting...")
buffer.wait()
}
buffer.enqueue(i)
println("Produced : " + i)
buffer.notifyAll()
}
Thread.sleep(500)
}
}
}
val consumer = new Thread {
override def run(): Unit = {
for (i <- 1 to 10) {
buffer.synchronized {
while (buffer.isEmpty) {
println("Buffer empty, consumer waiting...")
buffer.wait()
}
val item = buffer.dequeue()
println("Consumed : " + item)
buffer.notifyAll()
}
}
}
}
def main(args: Array[String]): Unit = {
producer.start()
consumer.start()
producer.join()
consumer.join()
println("Completed")
}
}