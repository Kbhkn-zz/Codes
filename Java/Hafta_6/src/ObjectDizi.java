public class ObjectDizi {
	public static void main(String[] args) {
		Object dizi[] = new Object[5];
		dizi[0] = "Hakan";
		dizi[1] = 2;
		dizi[2] = 444.5;
		for(int i=0;i<3;i++){
			//System.out.println((i+1) + ".eleman "+ dizi[i]);
		}
		/*double i = ((Integer) dizi[1]).intValue() + ((Double) dizi[2]).doubleValue();
		System.out.println(i);*/
		//System.out.println((int)(dizi[1]) + (double)(dizi[2]));
		int liste[] = {1,2,3,4,5};
		liste = new int[15];
		liste = new int[5];
		System.out.println(liste[2]);
		//System.out.println(liste[14]);
	}
}