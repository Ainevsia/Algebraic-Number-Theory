#ifndef __INTEGER_H__
#define __INTEGER_H__

#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

/**
 * This class **integer** is the basic definiion of the integer
 * it cannot support negative numbers now
 * (size) can have a negative value to show it is a negative number
 * the only operator it now has is the + operator
 *
 * i want to make it into a commond line tool in future
 * there is huge amount of things to do.
 */

class integer {
private:
    int size; // to track the length (how many digits) in the integer
    char* data; // use a char to represent every sigle digit
public:
    integer(){};
    integer(char sign){};
    integer(char* init_str);
    integer(char* data_a, char* data_b);
    ~integer();
    void display();
    char* getdata() { return data; };
    int getsize() { return size; };
    bool operator==(integer& b);
    bool operator!=(integer& b);
    bool operator>(integer& b);
    integer operator+(integer& b); // key operator then
};

integer::integer(char* init_str)
{
    data = new char[LONG_MAX];
    if (!init_str) {
        size = 0;
    } else {
        size = strlen(init_str);
        for (int i = 0; i < size; i++) {
            data[i] = init_str[size - i - 1];
        }
    }
}

//
integer::integer(char* data_a, char* data_b)
{
    data = new char[LONG_MAX];
    int size_a = strlen(data_a == NULL ? "" : data_a);
    int size_b = strlen(data_b == NULL ? "" : data_b);
    size = size_a > size_b ? size_a : size_b;
    if (size_a > size_b) {
        for (int i = 0; i < size; i++) {
            data[i] = data_a[i];
        }
    } else {
        for (int i = 0; i < size; i++) {
            data[i] = data_b[i];
        }
    }
}

integer::~integer()
{
    if (data)
        delete[] data;
}

void integer::display()
{
    if (size < 0)
        cout << '-';
    // else if (size > 0) cout << '+';
    size = abs(size);
    for (int i = size - 1; i >= 0; i--) {
        cout << data[i];
    }
    cout << endl;
}

bool integer::operator==(integer& b)
{
    bool ret = true;
    int size_a = this->size;
    int size_b = b.getsize();
    char* data_a = this->data;
    char* data_b = b.getdata();
    if (size_a != size_b) {
        ret = false;
    } else if (size_a == size_b) {
        for (int i = 0; i < size_a; i++) {
            if (data_a[i] != data_b[i]) {
                ret = false;
                break;
            }
        }
    }
    return ret;
}

// passing the param must be **&** param!
bool integer::operator!=(integer& b)
{
    return !(this->operator==(b));
}

bool integer::operator>(integer& b)
{
    bool ret = true;
    int size_a = this->size;
    int size_b = b.getsize();
    char* data_a = this->data;
    char* data_b = b.getdata();
    if (size_a < size_b)
        ret = false;
    else if (size_a > size_b)
        ret = true;
    else if (size_a == size_b) {
        int i = 0;
        for (i = size_a; i >= 0; i--) {
            if (data_a[i] < data_b[i]) {
                ret = false;
                break;
            }
        }
        if (i == -1 && ret)
            ret = false;
    }
    return ret;
}

integer
integer::operator+(integer& b)
{
    integer ret(this->data, b.getdata());
    integer* st = this->getsize() > b.getsize() ? &b : this;
    bool carry = false;
    int end = st->getsize(), i;
    char digit;
    for (i = 0; i < end; i++) {
        digit = ret.data[i] + st->data[i] - '0';
        if (carry)
            digit++;
        if (digit > '9') {
            carry = true;
            ret.data[i] = digit - 10;
        } else {
            carry = false;
            ret.data[i] = digit;
        }
    }
    // 10 + 999999999
    for (; carry; i++) {
        if (i == ret.size && carry) {
            ret.data[ret.size] = '1';
            ret.size = ret.size + 1;
        }
        digit = ret.data[i] + 1;
        if (digit > '9') {
            ret.data[i] = digit - 10;
        } else {
            carry = false;
        }
    }
    return ret;
}

// integer integer::operator*(integer& b) {
//     integer ret('+');
//     return ret;
// }
#endif