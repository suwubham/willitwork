#include <iostream>
#include <string>
using namespace std;
class nums{
    public:
    int x,y;
    nums(int z){
        x = z;
    }
};
int main(){
    nums n1(5);
    cout << n1.x << endl << n1.y;

return 0;
}