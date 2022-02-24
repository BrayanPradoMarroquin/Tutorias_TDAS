/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listas;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import listas.ListaSimple;
/**
 *
 * @author Usuario
 */
public class LISTAS {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        String json = "";
        
        try {
            BufferedReader br = new BufferedReader(new FileReader("ejemplo.json"));
            
            String linea = "";
            
            while ((linea = br.readLine()) != null) {
                json += linea;
            }
            br.close();
            
            } catch (FileNotFoundException ex) {
                Logger.getLogger(LISTAS.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        //System.out.println(json);
    }
    
}
