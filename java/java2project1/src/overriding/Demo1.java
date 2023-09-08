package overriding;

public abstract class Demo1 {
    public abstract void method1();

    public void method2() {
        System.out.println("Method 2.");
    }

    public abstract void method3();
}

class Demo2 extends Demo1 {
    public void method1() {
        System.out.println("Method1.");
    }

    @Override
    public void method3() {
        System.out.println("Method3.");
    }


}