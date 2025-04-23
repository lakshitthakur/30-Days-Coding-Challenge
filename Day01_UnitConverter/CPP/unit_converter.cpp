#include <iostream>
using namespace std;

int main() {
    int choice;
    double input;

    cout << "Unit Converter:" << endl;
    cout << "1. cm to inches" << endl;
    cout << "2. kg to pounds" << endl;
    cout << "3. Celsius to Fahrenheit" << endl;
    cout << "Enter choice (1-3): ";
    cin >> choice;

    switch (choice) {
        case 1:
            cout << "Enter cm: ";
            cin >> input;
            cout << input << " cm = " << input / 2.54 << " inches" << endl;
            break;
        case 2:
            cout << "Enter kg: ";
            cin >> input;
            cout << input << " kg = " << input * 2.20462 << " pounds" << endl;
            break;
        case 3:
            cout << "Enter Celsius: ";
            cin >> input;
            cout << input << " °C = " << (input * 9 / 5) + 32 << " °F" << endl;
            break;
        default:
            cout << "Invalid choice." << endl;
    }

    return 0;
}
