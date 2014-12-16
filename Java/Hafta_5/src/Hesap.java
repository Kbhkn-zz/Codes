package Box;

public class Hesap {
	static double volume(Box1 ref){
		return ref.depth*ref.heigth*ref.width;	
	}
	double squart(double w, double h){
		return h*w;
	}
	void yazdir(double hacim, double alan){
			System.out.println("Hacim = " + hacim);
			System.out.println("Hacim = " + alan);
		}
	}