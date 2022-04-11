// Java Program to Check Fermat’s Little Theorem
import java.util.*;
class fermat{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the value of a: ");
    int a = sc.nextInt();
    System.out.println("Enter the value of p: ");
    int p = sc.nextInt();
    
    checkFermat(a, p);
  }
  static int checkFermat(int a, int p){
    int n = (int) Math.pow(a, p-1) % p;
    if(n==1) System.out.println("Fermat's Little Theorem holds true");
    else System.out.println("Fermat's Little Theorem holds false");
    return n;
  }
  // static void modularInverse(int a, int p){
  //   if(checkFermat(a, p)!=1) System.out.println("Inverse does not exist");
  //   else{
  //     int inverse = (int) Math.pow(a, p-2) % p;
  //     System.out.println("Modular Multiplicative Inverse is: "+inverse);
  //   }
  // }
}