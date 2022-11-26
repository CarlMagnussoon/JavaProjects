import java.util.ArrayList;

public class GenerateSecretSanta {

	public static void main(String[] args) {
		
	ArrayList<person> familymembers= new ArrayList<person>();
	
		for (int i =0; i<args.length;i++) {
			familymembers.add(new person(args[i]));
		}
		for (int i =0; i<familymembers.size();i++) {
			familymembers.get(i).generateSanta(familymembers);
		}

		
	}

}
