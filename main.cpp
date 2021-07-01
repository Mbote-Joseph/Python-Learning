#include <iostream>
using namespace std;
int main(){
    int totalDistance;
    int distanceJumped;
    cout<<"How Much distance to cover : "<<endl;
    cin>>totalDistance;
    cout<<"How Much it can jump : "<<endl;
    cin>>distanceJumped;
   for(int j=distanceJumped; j<totalDistance; j+distanceJumped){
       int times=totalDistance/distanceJumped;
      for (int i=1; i<=times; i++){
      cout<<"After Jump #"<<i<<" : "<< j<<endl;
      }
   }
   return 0;
}