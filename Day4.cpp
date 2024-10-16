#include <iostream>
using namespace std;

int main() {
    int ip;
    cout << "Enter a number: ";
    cin >> ip;

    if (ip > 0) {
        cout << ip << " is a positive number" << endl;
    }
    else if (ip < 0) {
        cout << ip << " is a negative number" << endl;
    }
    else {
        cout << "Neither negative nor positive" << endl;
    }

    return 0;
}

// time and space complexity O(1)