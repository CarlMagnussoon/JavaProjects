import java.util.ArrayList;

public class Device {
	private String name, duration, finalrisk;
	private boolean active, invasive;
	private ArrayList<String> additional, riskclass; //riskclass
	private ArrayList<Paragraph> paragraphs; //denna kommer vara alla paragrafer
	
	//Constructors
	public Device (){
		
	}
	
	public Device (String name, boolean invasive, boolean active, String duration, ArrayList<String> riskclass, ArrayList<String> additional, ArrayList<Paragraph> paragraphs) {
		this.name = name;
		this.active=active;
		this.invasive = invasive;
		this.duration = duration;
		this.riskclass = riskclass;
		this.additional=additional;
		this.paragraphs = paragraphs;
	}
	//Getters and Setters
	
	public void setName (String name) {

		this.name = name;
	}
	
	public String getName() {

		return this.name;
	}
	
	public void setDuration(String duration) {
		this.duration = duration;
	}
	
	public String getDuration() {
		return this.duration;
	}
	
	public void setRiskclass(String risk) {
		this.riskclass.add(risk);
	}
	
	public ArrayList<String> getRiskclasses() {
		return this.riskclass;
	}

	public boolean getActive() {
		return active;
	}
	public void setActive(boolean active) {
		this.active = active;
	}
	
	public boolean getInvasive() {
		return invasive;
	}
	
	public void setInvasive(boolean invasive) {
		this.invasive = invasive;
	}

	public ArrayList<String> getAdditional() {
		return additional;
	}

	public void setAdditional(ArrayList<String> additional) {
		this.additional = additional;
	}
	public ArrayList<Paragraph> getParagraphs() {
		return paragraphs;
	}

	public void setParagraphs(ArrayList<Paragraph> paragraphs) {
		this.paragraphs = paragraphs;
	}
	
	//Kollar både additional och type
	/*
	 * public ArrayList<Paragraph> compileApplicableParagraphs(){
	 * 
	 * ArrayList<Paragraph> para = new ArrayList<Paragraph>();
	 * 
	 * 
	 * for (int j = 0 ; j<this.additional.size(); j++) { for (int i = 0;
	 * i<paragraphs.size();i++) { if (this.type.get(j) ==
	 * paragraphs.get(i).getType() || this.additional.get(j) ==
	 * paragraphs.get(i).getAdditional()) { para.add(paragraphs.get(i)); } else {
	 * paragraphs.get(i).changeStatus(); } } } return para; }
	 * 
	 * public ArrayList<Paragraph> getApplicableParagraphs(){
	 * 
	 * return compileApplicableParagraphs(); }
	 */
	
	
	//metoden sorterar från registret och kommer bara innehålla de applicerbara paragraferna från själva registret. 
	//måste även ha en lista på paragraferna efter man gått igenom vyn.
	//Behöver egentligen inte returnera något, utan kan bara ändra devicens paragrafer. 
	public void sortParagraphs(){
		
		ArrayList<Paragraph> para = new ArrayList<Paragraph>();
		
		for (int i = 0; i<paragraphs.size();i++) {
			
			if (this.invasive && this.active && paragraphs.get(i).getActive() && paragraphs.get(i).getInvasive()) {
					para.add(paragraphs.get(i));
					this.setRiskclass(paragraphs.get(i).getRiskClass());
					paragraphs.get(i).changeStatus();
					
			} else if (this.invasive && paragraphs.get(i).getInvasive()) {
				para.add(paragraphs.get(i));
				this.setRiskclass(paragraphs.get(i).getRiskClass());
				paragraphs.get(i).changeStatus();
			} else if (this.invasive == false && paragraphs.get(i).getInvasive() == false) {
				para.add(paragraphs.get(i));
				this.setRiskclass(paragraphs.get(i).getRiskClass());
				paragraphs.get(i).changeStatus();
			} else if(this.active && paragraphs.get(i).getActive()) {
				para.add(paragraphs.get(i));
				this.setRiskclass(paragraphs.get(i).getRiskClass());
				paragraphs.get(i).changeStatus();
			} else if (this.active && paragraphs.get(i).getActive()) {
				para.add(paragraphs.get(i));
				this.setRiskclass(paragraphs.get(i).getRiskClass());
				paragraphs.get(i).changeStatus();
			}
			
			if(paragraphs.get(i).getSpecial() && para.contains(paragraphs.get(i))==false) {
				para.add(paragraphs.get(i));
				this.setRiskclass(paragraphs.get(i).getRiskClass());
				paragraphs.get(i).changeStatus();
			}		
	}
		//return para;
	}
	
	public ArrayList<Paragraph> getApplicableParagraphs(){
		ArrayList<Paragraph> para = new ArrayList<Paragraph>();
		
		for(int i=0 ; i<this.paragraphs.size();i++) {
			if(paragraphs.get(i).getStatus() == "Applicable") {
				para.add(paragraphs.get(i));
			}
		}
		
		return para;
	}
	
	
	//defines the final riskclass.
	public String getHighRiskClass() {
		if (this.riskclass.contains("III")) {
			finalrisk = "III";
		} else if(this.riskclass.contains("IIb")) {
			finalrisk = "IIb";
		} else if (this.riskclass.contains("IIa")) {
			finalrisk = "IIa";
		} else if (this.riskclass.contains("I")) {
			finalrisk = "I";
		} else {
			finalrisk = "Not classified as a Medical Device.";
		}
		return finalrisk;
	}

	
	
	
	
	
	
}
