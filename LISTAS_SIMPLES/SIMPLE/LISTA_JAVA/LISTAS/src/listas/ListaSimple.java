/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listas;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import listas.Nodo;
/**
 *
 * @author Usuario
 */
public class ListaSimple {
    private Nodo inicio;
    private int tamanio;
    
    //Crea el constructor de la clase ListaSimple
    public void ListaSimple(){
        inicio = null;
        tamanio = 0;
    }
    
    //Define si la lista esta vacia
    public boolean vacio(){
        return inicio == null;
    }
    
    //Define el tamanio de la lista
    public int tamanio(){
        return tamanio;
    }
    
    
    //Agrega los elementos al inicio de la lista
    public void agregarInicio(int id){
        Nodo nuevo = new Nodo();
        nuevo.setNombre(Nombre);
        if(vacio()){
            inicio = nuevo;
        }else{
            nuevo.setSiguiente(inicio);
            inicio = nuevo;
        }
        tamanio++;
    }
    
    
    //Imprime en consola los datos de la lista 
    public void listar(){
        if(!vacio()){
            Nodo aux = inicio;
            int i = 0;
            while(aux!=null){
                System.out.println("Valor: "+aux.getId());
                aux = aux.getSiguiente();
                i++;
            }
        }
    }
    
    //Grafica los elementos de la grafica
    public void graficar(){
        try {
            String Path = "Lista.dot";
            Nodo aux = inicio;
            File archivo = new File(Path);
            String encabezado = "digraph G{\n";
            while(aux!=null){
                encabezado = encabezado + "Node"+aux.getId()+"[label=\""+aux.getId()+"\"];\n";
                if(aux.getSiguiente()!=null){
                    encabezado=encabezado+"Node"+aux.getId()+" -> Node"+aux.getSiguiente().getId()+";\n";
                }
                aux = aux.getSiguiente();
            }
            encabezado = encabezado + "}";
            if(archivo.exists()){
                archivo.delete();
            }
            archivo.createNewFile();
            FileWriter escritura = new FileWriter(archivo);
            BufferedWriter bw = new BufferedWriter(escritura);
            bw.write(encabezado);
            bw.close();
            
            ProcessBuilder bb;
            bb = new ProcessBuilder("dot", "-Tpng", "-o", "ejemplo.png", Path);
            bb.redirectErrorStream(true);
            bb.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
