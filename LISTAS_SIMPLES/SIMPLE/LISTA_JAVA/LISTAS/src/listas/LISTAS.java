/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listas;
import listas.ListaSimple;
/**
 *
 * @author Usuario
 */
public class LISTAS {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Instancia un Objeto de la clase ListaSimple
        ListaSimple nueva = new ListaSimple();
        System.out.println("< --------- Listas ----------->");
        //Realiza las operaciones que se solicitan en la lista
        nueva.agregarInicio(0);
        nueva.agregarInicio(1);
        nueva.agregarInicio(2);
        nueva.agregarInicio(4);
        nueva.listar();
        nueva.graficar();
    }
    
}
