import java.util.ArrayList;

class carDetials{
    private String Brand;
    private String Model;
    private double Price;

    //Default Constructor
    public carDetials(){
        Brand = "Tata";
        Model = "Indica";
        Price = 400000;
    }

    //Parameterized Constructor
    public carDetials(String Brand, String Model, double Price){
        this.Brand = Brand;
        this.Model = Model;
        this.Price = Price;

    }
    public String getBrand(){
        return Brand;
    }

    public void setBrand(String Brand){
        this.Brand = Brand;
    }

    public String getModel(){
        return Model;
    }

    public void setModel(String Model){
        this.Model = Model;
    }

    public double price(){
        return Price;
    }

    public void setPrice(double Price){
        this.Price = Price;
    }

    public void displayCarDetails() {
        System.out.println("Brand: " + Brand + ", Model: " + Model + ", Price: " + Price);
    }

}


public class carDealerShip {

    ArrayList<carDetials> cars;

    public carDealerShip(){

       cars = new ArrayList<>();
    }

    public void addcar(carDetials car){
        cars.add(car);
    }

    public void display(){
        for (carDetials carDetials : cars) {
            carDetials.displayCarDetails();
        }
    }
    public static void main(String[] args){


        carDealerShip car = new carDealerShip();
        car.addcar(new carDetials("Honda", "Amaze", 900000));
        car.display();
        

    }
}
