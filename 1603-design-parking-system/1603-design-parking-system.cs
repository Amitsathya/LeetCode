class Vehicle{

}


public class ParkingSystem {
    private int big;
    private int medium;
    private int small;

    public ParkingSystem(int big, int medium, int small) {
        this.big = big;
        this.medium = medium;
        this.small = small;
    }
    
    public bool AddCar(int carType) {
        if (carType == 1){
            if (big > 0){
                big -= 1;
                return true;
            }
        } else if (carType == 2){
            if (medium > 0){
                medium -= 1;
                return true;
            }
        } else if (carType == 3){
            if (small > 0){
                small -= 1;
                return true;
            }
        }
        return false;        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */