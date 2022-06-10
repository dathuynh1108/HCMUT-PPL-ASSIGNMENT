
public class D96Class {
       public static void main(String[] args) {
              Animal a = new Dog();  
              a.eat();  
       }

}

class Animal {
       public void eat() {
              System.out.println("animal is eating...");
       }
}

class Dog extends Animal {
       public void eat() {
              System.out.println("dog is eating...");
       }
}
