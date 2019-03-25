#include <cmath>
#include <cstring>
#include <iostream>

#include "integer.h"

using namespace std;

/**
 * the main execution map
 */

int main(int argc, char const* argv[])
{
    // freopen("./test.txt", "r", stdin);
    char* in1 = new char[LONG_MAX];
    char* in2 = new char[LONG_MAX];
    cout << "This progarm can calculate the sum of any positive integer you give!!\nif Not believe and you can Have a try!!\n";
    cout << "please input a:" << endl;
    cin >> in1;
    cout << "please input b:" << endl;
    cin >> in2;
    integer a(in1);
    integer b(in2);
    cout << "a = ";
    a.display();
    cout << "b = ";
    b.display();
    integer c = a + b;
    c.display();
    return 0;
}
