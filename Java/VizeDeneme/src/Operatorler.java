
public class Operatorler {
	public static void main(String[] args) {
		int x =11, y=5, z=0, z1=0;
		z = x > y ? x:y; //x y'den büyük mü? Büyükse z=x Deðilse z=y
		z1 = x < y ? x:y;//x y'den büyük mü? Büyükse z1=x Deðilse z1=y
		System.out.println("z: " + z); //11
		System.out.println("z1: " + z1); //5
	}
}
