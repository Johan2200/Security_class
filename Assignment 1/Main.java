
public class Main {

    public static void main(String[] args) {
        
        // public parameters:
        int p = 29837;
        int g = 42;
        double pk = 22960;

        // I intercept:
        int c1 = 23447;
        int c2 = 8372;


        // Det her er ikke helt rigtigt
        for(int i = 1; i < 22690; i++){ 
            if ((Math.pow(g, i)) % p == pk){
                System.out.println(i);
            }
        }

    }
}