
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;


public class person {
	private String name;
	private String secretSanta;
	private boolean hasSanta;
	private boolean isSanta;
	private  ArrayList<String> presenter= new ArrayList<String>();
	
	
	
	public person() {
		this.hasSanta =false;
		this.isSanta=false;
	}
	public person(String name) {
		this.name = name;
		this.hasSanta=false;
		this.isSanta=false;
	}
	
	public String getName() {
		return this.name;
	}
	public void setName(String name) {
		this.name =name;
	}
	
	public String getsecretSanta() {
		return this.secretSanta;
	}
	public void setsecretSanta(String secretSanta) {
		this.secretSanta = secretSanta;
	}

	public boolean gethasSanta() {
		return this.hasSanta;
	}
	public void sethasSanta() {
		this.hasSanta = true;
	}

	public boolean getisSanta() {
		return this.isSanta;
	}
	public void setisSanta() {
		this.isSanta=true;
	}
	public void setPresenter(String present) {
		this.presenter.add(present);
	}
	
	public ArrayList<String> getPresenter(){
		return this.presenter;
	}

	public String getPresent(int i){
		return this.presenter.get(i);
	}
	
	public void generateSanta(ArrayList <person> familymembers) {
		Random rand = new Random();
		while (this.hasSanta == false) {
		int int_random = rand.nextInt(familymembers.size());
		if (familymembers.get(int_random).getisSanta() == false && familymembers.get(int_random).getName() != this.getName() ) {
				this.setsecretSanta(familymembers.get(int_random).getName());
				familymembers.get(int_random).setisSanta();
				this.sethasSanta();
				try {
					FileWriter myWriter;
					myWriter = new FileWriter("/Users/Carl/Desktop/Secret Santa Projekt/"+this.getName()+".txt");
					myWriter.write(this.getName()+ ", du ska vara Secret Santa till " +this.getsecretSanta());
					myWriter.close();
				} catch(IOException e) {
					e.printStackTrace();
				}

			} 
		}
	}
}
