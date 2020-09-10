#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    long long N;
    cin >> N;

    long long liquid[N];
    for(long i=0 ; i<N; i++){
        long long num;
        cin >> num;

        liquid[i] = num;
    }
    
    sort(liquid, liquid+N);
    long long close_zero[4];
    close_zero[0] = pow(10,10), close_zero[1] = 0, close_zero[2]=0, close_zero[3]=0;
    /* for(int i = 0 ; i<4; i++){
        cout << close_zero[i] << " ";
    } */

    for(long i=0 ; i<N-2 ; i++){
        long long start = i+1, end = N-1;
        if(abs(close_zero[0]) > abs(liquid[i] + liquid[start] + liquid[end])){
            close_zero[0] = liquid[i] + liquid[start] + liquid[end];
            close_zero[1] = i, close_zero[2]=start, close_zero[3]=end;
        }

        if(close_zero[0] == 0){
            break;
        }

        for (long j=0 ; j<N-2-start ; j++ ){
            if (close_zero[0] < 0) start += 1;  
            else end -= 1;

            if(start == end) break;
            
            if (abs(close_zero[0]) > abs(liquid[i] + liquid[start] + liquid[end])){
                close_zero[0] = liquid[i] + liquid[start] + liquid[end];
                close_zero[1] = i, close_zero[2]=start, close_zero[3]=end;
            }
            
            if(close_zero[0] == 0) break;
        }
        
        
    }
  
  
    /* for(int i = 0 ; i<4; i++){
        cout << close_zero[i] << " ";
    } */
    cout << endl << liquid[close_zero[1]] << " " <<  liquid[close_zero[2]] << " " << liquid[close_zero[3]];
}