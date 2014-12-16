public class ParDondurmeReturn {
	public static void BiseyYapma(double a){
		if(a==0)
			return; //Metot sonlandýrýlýr.
		else
			System.out.println("a = " +a);
	}
	public static void main(String[] args){
		System.out.println("Return deneme yapalim_bir: ");
		BiseyYapma(5);
		System.out.println("Return deneme yapalim_iki");
		//System.out.println(BiseyYapma(0.0));
	}
}