import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;


import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Register<E> extends ArrayList<E> {

	private static final long serialVersionUID = 1L;
	private ArrayList<Paragraph> register = new ArrayList<Paragraph>();
	
	public Register(){

	}
	
	public ArrayList<Paragraph> instantiateParagraphs(){


		for (int rows=1; rows<14;rows++) {
			//for (int rows=1; rows <=14 ;rows++) {}
			
			Paragraph para = new Paragraph();
			
			for (int cols=0; cols <5;cols++) {
				
				//switch sats som kollar vilket värde på kolumnen det är
				switch (cols){
				
				case 0:
					para.setParagraphnumber(ReadCellData(rows,cols));
					break;
				case 1:
					para.setText(ReadCellData(rows,cols));
					break;
				case 2:
					if(ReadCellData(rows, cols).equalsIgnoreCase("invasive")) {
						para.setInvasive(true);
					} else if (ReadCellData(rows, cols).equalsIgnoreCase("active")) {
						para.setActive(true);
					} else if(ReadCellData(rows, cols).equalsIgnoreCase("special")) {
						para.setSpecial(true);
					}
					break;
				//Vad ska additional information innehålla?
					
				//case 3: 
					//para.setAdditional(ReadCellData(rows, cols));
				//	break;
				
				case 4:
					para.setRiskClass(ReadCellData(rows, cols));
					break;
				}
			}
			register.add(para);
		} return register;
		}
			
	
	
	

	
	public String ReadCellData(int vRow, int vCol) {
		String value = null;
		Workbook wb = null;
		try {
			FileInputStream fis = new FileInputStream("/Users/Carl/Desktop/Projekt-MDR/Paragraphs/Paragrafer.xlsx");
			wb = new XSSFWorkbook(fis);
		}
		catch(FileNotFoundException e) {
			e.printStackTrace();
		}
		catch(IOException e1) {
			e1.printStackTrace();
		}
		
		Sheet sheet = wb.getSheetAt(0);
		Row row = sheet.getRow(vRow);
		Cell cell = row.getCell(vCol);
	
		
		switch(cell.getCellTypeEnum()) {
		case NUMERIC:
			value = Double.toString(cell.getNumericCellValue());
			break;
		case STRING:
			value = cell.getStringCellValue();
			break;
		case BLANK:
			value = null;
			break;
		case BOOLEAN:
			break;
		case ERROR:
			break;
		case FORMULA:
			break;
		case _NONE:
			break;
		default:
			break;
			}
		return value;
		}
	

}
