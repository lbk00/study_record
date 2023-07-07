> 클래스를 통해 객체를 생성할때, 객체가 유일한 하나만 생성되도록 만드는 것

class Singleton {

    private static Singleton one;
    private Singleton() {
    }

    public static Singleton getInstance() {
        if(one==null) { // 객체가 생성되지않은 상태이면
            one = new Singleton(); //객체를 생성
        }
        return one;
    }
}

public class Sample {

    public static void main(String[] args) {
    
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();
        System.out.println(singleton1 == singleton2);  // true 출력
    }
}
