public class Armstrong {
	public static void main(String[] args) {
		
		int YuzB, OnB, BirB, YuzKup, OnKup, BirKup;
		
		System.out.println("100-999 arasýndaki Armstrong sayýlarý:");
		System.out.println("--------------------------------------") ;
		
		for(int i=100;i<1000;i++){
			YuzB = i/100;
			OnB = (i-(YuzB*100))/10;
			BirB = i-(YuzB*100+OnB*10);
			YuzKup = YuzB*YuzB*YuzB;
			OnKup = OnB*OnB*OnB;
			BirKup = BirB*BirB*BirB;
			
			if(i == (YuzKup+OnKup+BirKup))
				System.out.println(i);
		}
	}
}