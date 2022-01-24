import java.io.*;
import javax.swing.JOptionPane;
/**
 *
 * @author juanea
 */
public class main_reversa_cadena {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String cadenaInicial="",cadenaRevertida="";
        char caracter=' ';
        cadenaInicial=JOptionPane.showInputDialog(null,"Digite una cadena para revertir","CAPTURA DE DATOS",JOptionPane.QUESTION_MESSAGE);
        System.out.println("La cadena ingresada fue: "+cadenaInicial+"\n");
        for (int counter=0;counter<cadenaInicial.length();counter++){
        caracter=cadenaInicial.charAt(counter);
        cadenaRevertida=caracter+cadenaRevertida;
        }
        JOptionPane.showMessageDialog(null,"El resultado de revertir la cadena ingresada fue: "+cadenaRevertida,"RESULTADO",JOptionPane.INFORMATION_MESSAGE);
        System.out.println("El resultado de revertir la cadena ingresada fue: "+cadenaRevertida);
    }
    
}
