abstract class Smartphone(
val brandName: String,
val version: String,
val ram: String,
val cameraPixel: String,
val weight: String,
val thickness: String,
val chipType: String,
val displayType: String,
val height: String,
val width: String,
val simType: String
) {
def displayInfo(): Unit = {
println("Brand: " + brandName)
println("Version: " + version)
println("RAM: " + ram)
println("Camera: " + cameraPixel)
println("Weight: " + weight)
println("Thickness: " + thickness)
println("Chip Type: " + chipType)
println("Display Type: " + displayType)
println("Height: " + height)
println("Width: " + width)
println("SIM Type: " + simType)
println("-------------------------")
}
}
class SamsungPhone extends Smartphone(
"Samsung", "Galaxy S25 Ultra", "12GB", "200MP", "218g",
"7.2mm", "Snapdragon", "AMOLED", "162.8mm", "77.6mm",
"Nano-SIM"
)
class ApplePhone extends Smartphone(
"Apple", "iPhone 17", "8GB", "48MP", "177g",
"7.8mm", "A19", "Super Retina XDR", "149.6mm", "71.5mm",
"eSIM"
)
class OnePlusPhone extends Smartphone(
"OnePlus", "OnePlus 13", "12GB", "50MP", "210g",
"8.5mm", "Snapdragon", "AMOLED", "162.9mm", "76.5mm",
"Dual Nano-SIM"
)
object SmartphoneDemo {
def main(args: Array[String]): Unit = {
val samsung = new SamsungPhone()
val apple = new ApplePhone()
val oneplus = new OnePlusPhone()
samsung.displayInfo()
apple.displayInfo()
oneplus.displayInfo()
}
}