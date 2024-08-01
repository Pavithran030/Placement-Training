import java.util.Scanner;
class Main{
    public static int odd(int a){
        if (a%2==0){
            return 1;
        }
        else{
            return 0;
        }
    }
    public static void main( String [] args){
        Scanner ob=new Scanner(System.in);
        System.out.print("Enter a number : ");
        int a=ob.nextInt();
        int k=odd(a);
        if (k==1){
            System.out.print("Even");
        }
        else{
            System.out.print("Odd");
        }
        
    }
}
