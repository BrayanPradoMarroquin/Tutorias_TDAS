/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listas;

/**
 *
 * @author Usuario
 */
public class Nodo {
    private int edad;
    private String nombre;
    private String[] aficiones;

    public Nodo(int edad, String nombre, String[] aficiones) {
        this.edad = edad;
        this.nombre = nombre;
        this.aficiones = aficiones;
    }

    public Nodo() {
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String Nombre) {
        this.nombre = Nombre;
    }

    public String[] getAficiones() {
        return aficiones;
    }

    public void setAficiones(String[] aficiones) {
        this.aficiones = aficiones;
    }

    @Override
    public String toString() {
        return "Nodo{" + "edad=" + edad + ", Nombre=" + nombre + ", aficiones=" + aficiones + '}';
    }
    
    
}
