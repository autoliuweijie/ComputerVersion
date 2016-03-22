//
// @authoer: Liu Weijie
// @date: 2016-03-21
//
#include <string>
#include <iostream>
#include <vector>


using namespace std;


int main(int argc, char** argv) {

    vector<char> charVector;
    charVector.push_back('A');
    charVector.insert(charVector.begin(),'B');
    charVector[1] = 'C';
    cout << charVector[1] << endl;

    return 0;
}