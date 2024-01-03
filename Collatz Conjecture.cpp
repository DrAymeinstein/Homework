// Collatz Conjecture for every positive integer
#include <iostream>

using namespace std;

long long int i;
long long int card;

void collatz() {
    cout << "C(" << i << ") = {";
    cout << i << " ";
    while (i > 1) {
        if (i % 2 == 0) {
            i /= 2;
            cout << i << " ";
        } else {
            i = 3 * i + 1;
            cout << i << " ";
        }
        card++;
    }
    cout << "}" << endl;
    
}

int main() {
    cout << "Enter a number: ";
    cin >> i;

    if (i >= 1) {
        card = 1;
        collatz();
        cout << "There's " << card << " operations." << endl;
        cout << "Choose another number: ";
        cin >> i;
    } else {
        cout << "Error: input less than 1." << endl;
        cout << "Choose another number: ";
        cin >> i;
        if (i > 0) {
            return 0;
        }
    }

    return 0;
}
