""" Java Пример 1

import java.util.Arrays;
import java.util.List;

public class LambdaExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

        // Сортировка по длине имени с использованием лямбда-выражения
        names.sort((name1, name2) -> Integer.compare(name1.length(), name2.length()));

        // Вывод отсортированного списка
        names.forEach(System.out::println);
    }
}


Java Пример 2 -> интерфейс
// Определение функционального интерфейса с одним абстрактным методом
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
}

Java Пример 2 -> Main
public static void main(String[] args) {
        // Использование лямбда-выражения для создания экземпляра функционального интерфейса
        Calculator addition = (a, b) -> a + b;
        Calculator subtraction = (a, b) -> a - b;
        Calculator multiplication = (a, b) -> a * b;
        Calculator division = (a, b) -> (b != 0) ? a / b : 0; // Защита от деления на ноль

        // Вызов методов интерфейса с использованием лямбда-выражений
        System.out.println("Сложение: " + addition.calculate(5, 3));
        System.out.println("Вычитание: " + subtraction.calculate(8, 2));
        System.out.println("Умножение: " + multiplication.calculate(4, 6));
        System.out.println("Деление: " + division.calculate(10, 2));
    }
"""
