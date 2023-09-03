
public class Paragraph {
	
	private String  text, riskclass, paragraphnumber;
	private boolean invasive, active, special;
	private String status= "N/A";
	
	public Paragraph() {
			
		}
		
	 public Paragraph(boolean invasive, boolean active, boolean special, String text, String riskclass, String paragraphnumber) {
		 this.invasive = invasive;
		 this.active = active;
		 this.text = text;
		 this.riskclass = riskclass;
		 this.paragraphnumber=paragraphnumber;
		 this.special =  special;
		  
	 }

	public boolean getInvasive() {
		return this.invasive;
	}
	
	public void setInvasive(boolean invasive) {
		this.invasive = invasive;
	}
	
	public boolean getActive() {
		return this.active;
	}
	
	public void setActive(boolean active) {
		this.active = active;
	}
	
	public boolean getSpecial() {
		return this.special;
	}
	
	public void setSpecial(boolean special) {
		this.special = special;
	}
	 
	 public void setText(String text) {
		 this.text = text;
	 }
	 public String getText() {
		 return this.text;
	 }

	 public void setRiskClass(String riskclass) {
		 this.riskclass = riskclass;
	 }
	 public String getRiskClass() {
		 return this.riskclass;
	 }

	 public String getParagraphnumber() {
		return paragraphnumber;
	}	 
	 public void setParagraphnumber(String paragraphnumber) {
		this.paragraphnumber = paragraphnumber;
	}

	 
	 public void changeStatus() {
		 if (this.status == "N/A") {
			 this.status = "Applicable";
			 }
		 else {
			 this.status = "N/A";
		 }
	 }
	 
	 public String getStatus() {
		 return this.status;
	 }

	 public String toString() {
		 String str;
		 str = "ID: "+this.getParagraphnumber()+ ". Text: "+this.getText()+". Active: " +this.getActive()+". Invasive:" +this.getInvasive()+". Riskclass: " +this.getRiskClass();
		 return str;
	 }


	 
	 
	 
	 
}



