#include <iostream>
using namespace std;
int main(){
    string filename = "C:\\Users\\shubh\\Desktop\\experiments\\exp1.py";
    string command = "python ";
    command += filename;
    system(command.c_str());
    return 0;
}