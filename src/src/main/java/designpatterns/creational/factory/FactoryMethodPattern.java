package designpatterns.creational.factory;

public class FactoryMethodPattern {
    public static void main(String[] args) {
        Logistics roadLogistics = new RoadLogistics();
        roadLogistics.planDelivery();  // Output: Delivering cargo by land in a truck.

        Logistics seaLogistics = new SeaLogistics();
        seaLogistics.planDelivery();  // Output: Delivering cargo by sea in a ship.
    }
}
interface Transport {
    void deliver();
}

// Step 2: Implement Concrete Product Classes
class Truck implements Transport {
    @Override
    public void deliver() {
        System.out.println("Delivering cargo by land in a truck.");
    }
}

class Ship implements Transport {
    @Override
    public void deliver() {
        System.out.println("Delivering cargo by sea in a ship.");
    }
}

// Step 3: Define the Creator Class
abstract class Logistics {
    // Factory Method: Returns a product (Transport)
    abstract Transport createTransport();

    // Business logic using the factory method
    public void planDelivery() {
        Transport transport = createTransport();
        transport.deliver();
    }
}

// Step 4: Implement Concrete Creator Classes
class RoadLogistics extends Logistics {
    @Override
    Transport createTransport() {
        return new Truck(); // Returns a Truck instance
    }
}

class SeaLogistics extends Logistics {
    @Override
    Transport createTransport() {
        return new Ship(); // Returns a Ship instance
    }
}
