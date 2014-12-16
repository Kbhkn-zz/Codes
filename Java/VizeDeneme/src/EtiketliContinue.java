public class EtiketliContinue {
	public static void main(String[] args){
		kiril:
		for(int j=0;j<4;j++){
			for(int i=0;i<5;i++){
				if(i == 1)
					continue kiril;
				System.out.println("i= " +i);
			}
			System.out.println("Döngü sonu");
		}
	}
}