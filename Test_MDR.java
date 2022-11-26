
import java.util.*;

public class Testing {
	
	public static void main(String[] args) {
		String name, duration;
		ArrayList<String> type = new ArrayList<String>();
		ArrayList<String> riskclass = new ArrayList<String>();
		ArrayList<String> additional = new ArrayList<String>();
		ArrayList<Paragraph> paragraphs = new ArrayList<Paragraph>();
		name = "Test";
		duration = "Transient";
		type.add("Invasive");
		additional.add("Software");
		
		Paragraph para1 = new Paragraph(true, true ,true, "Active, Invasive and Special rule", "3","1");
		Paragraph para2 = new Paragraph(true, true, false,"Active, Invasive but not special","2b","2");
		Paragraph para3 = new Paragraph(true, false, false,"Invasive but neither active nor special","2a","3");
		Paragraph para4 = new Paragraph(false, true, false,"Active but not invasive or special", "1","4");
		
		paragraphs.add(para1);
		paragraphs.add(para2);
		paragraphs.add(para3);
		paragraphs.add(para4);
		
		//Paragraphs pars = new Paragraphs();
		//paragraphs = pars.instantiateParagraphs();
	
		
		

		//
		
		//for (int i = 0; i<para.size();i++) {
		//	System.out.println(para.get(i).getText());
		//	dev.setRiskclass(para.get(i).getRiskClass());
		//}
		
	 
		
		Register<Paragraph> pars = new Register<Paragraph>();
		ArrayList<Paragraph> paras = new ArrayList<Paragraph>();
		
		paras = pars.instantiateParagraphs();
		Device dev = new Device(name, true, false, duration, riskclass, additional, paras);
		dev.sortParagraphs();
		ArrayList <Paragraph> para = dev.getApplicableParagraphs();
		
		for (int i =0; i<para.size();i++) {
		System.out.println(para.get(i).toString());
		}
		
		   System.out.println(dev.getRiskclasses());
		   System.out.println(dev.getHighRiskClass());
		
		
	}
}
