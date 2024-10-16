#include <iostream>
using namespace std;

int main() {
    char ip;
    cout << "Please enter a character to check ASCII value for: ";
    cin >> ip;
    cout << "ASCII value of " << ip << " is " << int(ip) << endl;
    return 0;
}