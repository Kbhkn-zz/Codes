package Box;
	
public class MyBox{
	public static void main(String[] args){
		Box1 box1 = new Box1();
		Hesap y = new Hesap();
		box1.depth=4;
		box1.heigth=3;
		box1.width=2;
		y.yazdir(Hesap.volume(box1),y.squart(box1.depth, box1.heigth));
	}
}