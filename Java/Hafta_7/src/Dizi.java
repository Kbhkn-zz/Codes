public class Dizi{
	public static void main(String[] args){
		String dizi[] = {"Mehmet", "Hakan", "SalihCan"};
		System.out.println("Ýsimler: ");
		for(int i=0;i<3;i++)
			yazdir(i,dizi[i]);
	}
	
	static void yazdir(int sira, String eleman){
		System.out.println((sira+1) + ".kiþi " + eleman);
	}
}