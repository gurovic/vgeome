import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


class Point {
    public double x, y;

    Point(double first, double second) {
        x = first;
        y = second;
    }

    public String toString() {
        return "Coordinates: " + Double.toString(x) + ", " + Double.toString(y);
    }

    public Point neg() {
        Point newPoint = new Point(-x, -y);
        return newPoint;
    }

    public Point add(Vector otherVector) {
        Point newPoint = new Point(x + otherVector.x, y + otherVector.y);
        return newPoint;
    }
}


class Vector {
    public double x, y;

    Vector(double first, double second) {
        x = first;
        y = second;
    }

    Vector(Point first, Point second) {
        x = second.x - first.x;
        y = second.y - first.y;
    }

    public String toString() {
        return "Coordinates: " + Double.toString(x) + ", " + Double.toString(y);
    }

    public double abs() {
        return Math.pow(x * x + y * y, 0.5);
    }

    public Vector mul(double otherNumber) {
        Vector newVector = new Vector(x * otherNumber, y * otherNumber);
        return newVector;
    }

    public Vector add(Vector otherVector) {
        Vector newVector = new Vector(x + otherVector.x, y + otherVector.y);
        return newVector;
    }

    public Vector div(double otherNumber) {
        Vector newVector = new Vector(x / otherNumber, y / otherNumber);
        return newVector;
    }
    public Vector sub(Vector otherVector) {
        Vector newVector = new Vector(x - otherVector.x, y - otherVector.y);
        return newVector;
    }

    public double productVector(Vector otherVector) {
        return x * otherVector.y - y * otherVector.x;
    }

    public double productScalar(Vector otherVector) {
        return x * otherVector.x + y * otherVector.y;
    }
}


class Line {
    public double A, B, C;

    Line(double first, double second, double third) {
        A = first;
        B = second;
        C = third;
    }

    Line(Point first, Point second) {
        A = first.y - second.y;
        B = second.x - first.x;
        C = first.x * second.y - first.y * second.x;
    }

    public double dist(Point otherPoint) {
        return (A * otherPoint.x + B * otherPoint.y + C) / Math.pow((A * A + B * B), 0.5);
    }

    public Point[] cross(Line otherLine) {
        if (A * otherLine.B != B * otherLine.A) {
           Point crossPoint = new Point((B * otherLine.C - C * otherLine.B) / (A * otherLine.B - B * otherLine.A),
                                        (C * otherLine.A - A * otherLine.C) / (A * otherLine.B - B * otherLine.A));
           Point[] crossPoints = {crossPoint};
        return crossPoints;
    }
}


class Circle {
    public Point O;
    public double radius;

    Circle(Point first, double second) {
        O = first;
        radius = second;
    }
}


class Triangle {
    public Point A, B, C;
    public Vector AB, BA, AC, CA, BC, CB;

    Triangle(Point first, Point second, Point third) {
        A = first;
        B = second;
        C = third;
    }

    public double orientedArea() {
        return AB.productVector(AC) / 2;
    }
}


public class Hello {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        double number1 = Double.parseDouble(in.readLine());
        double number2 = Double.parseDouble(in.readLine());
        double number3 = Double.parseDouble(in.readLine());
        double number4 = Double.parseDouble(in.readLine());
        double number5 = Double.parseDouble(in.readLine());
        Point myp1 = new Point(number1, number2);
        Point myp2 = new Point(number3, number4);
        Vector myv1 = new Vector(myp1, myp2);
        System.out.println("first point: " + myp1.toString() + "; " + "second point: " + myp2.toString());
        System.out.println("vector " + myv1.toString());
        System.out.println("vector length: " + myv1.abs());
        System.out.println("new coordinats of first points: " + myp1.add(myv1.mul(number5)).toString());
    }
}
