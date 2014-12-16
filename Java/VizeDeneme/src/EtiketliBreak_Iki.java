public class EtiketliBreak_Iki {
	public static void main(String[] args){
		for(int i = 0; i<4; i++){
			label:
			for(int j = 0; j< 5; j++){
				for(int z = 0; z< 5; z++){
					if(z == 3)
						break label;
					System.out.println("i :"+i+" j :"+j+" z :"+z);
				}
			}
		}
		System.out.println("Döngü sonu");
	}
}