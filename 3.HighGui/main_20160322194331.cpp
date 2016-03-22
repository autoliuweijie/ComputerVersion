//
// @authoer: Liu Weijie
// @date: 2016-03-21
//
#include <string>
#include <iostream>

using namespace std;


template <class Type>
class People {

private:
    Type name;

public:
    People(Type name);
    void sayName();
};

template <class Type>
People<Type>::People(Type name_in) {
    name = name_in;
}

template <class Type>
void People<Type>::sayName() {
    cout << "My name is " << name << endl;
}


int main(int argc, char** argv) {

    People<string> xiaomin("xiaomin");
    xiaomin.sayName();
    return 0;
}