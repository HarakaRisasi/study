public class Lesson {
    public static void main(String[] args) {
        System.out.println(3 + 4);
        System.out.println(3 - 4);
        System.out.println(3 * 4);
        System.out.println(3 / 4);
        System.out.println(3 % 4);
        System.out.println(3 == 4);
        System.out.println(3 != 4);
        System.out.println(3 > 4);
        System.out.println(3 < 4);
        System.out.println(3 >= 4);
        System.out.println(3 <= 4);
        System.out.println(3 == 4 && 3 != 4);
        System.out.println(3 == 4 || 3 != 4);
        System.out.println(3 == 4 ^ 3 != 4);
        System.out.println(3 == 4 & 3 != 4);
        System.out.println(3 == 4 | 3 != 4);

        // Вывод на экран результата выражения 3 + 4 * 5
        System.out.println(3 + 4 * 5);     

        // Понимание композиции операций (порядка вычислений) и приоритета операторов 
        System.out.println(8 / 2 + 5 - -3 / 2);
        System.out.println((2 + 3) * 4 - 10 / 2);
        System.out.println(7 / 2 + 7 % 2);
        System.out.println(100 - 20 * 3 / 2 + 5);
        System.out.println((-5 + 3) * (8 / 3) - 2);

        // среднее арифметическое трёх чисел: 10, 15, 20
        System.out.println((10 + 15 + 20) / 3);
    }
}
