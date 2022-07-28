namespace CSharp;
class Program
{
    static void Main(string[] args)
    {
        printf("Hello, World!");

        string? firstName, lastName;

        print("First name: ");
        firstName = Console.ReadLine();

        print("Last name: ");
        lastName = Console.ReadLine();

        printf($"Full name: {firstName} {lastName}.");

        int numberOne, numberTwo, sum;

        numberOne = 45;
        numberTwo = 50;
        sum = numberOne + numberTwo;

    }

    static void print(string msg) {

        Console.Write(msg);
    }
    static void printf(string msg) {

        Console.WriteLine(msg);
    }

}
