#include <iostream>
#include <string>
using namespace std;
class userData{
    string name;
    int happy;
    public:
    userData();
    void show(void);
};
userData :: userData() : name("root"), happy(69){}
void userData ::  show(void){
    cout << "Name: " << name;
    cout << "\nHapppy: " << happy;
}
int main(){
    userData user1;
    user1.show();

    return 0;
}