import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

class Point {
    public double x, y;

    Point(double first, double second) {
        x = first;
        y = second;
    }

    public String str() {
        return ("Coordiants: " + Double.toString(x) + ", " + Double.toString(y));
    }

    public Point neg() {
        Point otherPoint = new Point(-x, -y);
        return (otherPoint);
    }
}


class Vector {
    public double x, y;
    public Point A, B;

    Vector(double first, double second) {
        x = first;
        y = second;
    }

    Vector(Point first, Point second) {
        A = first;
        B = second;
        x = B.x - A.x;
        y = B.y - A.y;
    }

    public String str() {
        return ("Coordiants: " + Double.toString(x) + ", " + Double.toString(y));
    }

    public double abs() {
        return (Math.pow(x * x + y * y, 0.5));
    }
}


public class Hello {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        double number1 = Double.parseDouble(in.readLine());
        double number2 = Double.parseDouble(in.readLine());
        double number3 = Double.parseDouble(in.readLine());
        double number4 = Double.parseDouble(in.readLine());
        Point myp1 = new Point(number1, number2);
        Point myp2 = new Point(number3, number4);
        Vector myv1 = new Vector(myp1, myp2);
        System.out.println(myp1.str() + "; " + myp2.str());
        System.out.println(myv1.str());
        System.out.println(myv1.abs());
    }
}
