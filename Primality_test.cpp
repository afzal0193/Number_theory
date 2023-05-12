/*
Primality-test Related problems :- 
1.https://www.codechef.com/problems/PRB01
2.https://lightoj.com/problem/dimik-is-prime
3.https://toph.co/p/is-prime
4.https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/little-shino-and-prime-difference-38c91b0d/

*/


#include<bits/stdc++.h>
using namespace std;

bool prime(long  n){
	
	if(n<2){
		return false;
	}
	if(n<=3){
		return true;
	}
	if(n%2==0){
		return false;
	}
	 
	for(int i = 3;i<=sqrt(n); i +=2){
		if(n%i ==0){
			return false;
		}
	 }
	 
	 return true;
	 
}

int main(){
	int t;
	cin>>t;
	while(t--){
		long n;cin>>n;
		if(prime(n)){
			cout<<n<<" is Prime number"<<endl;
		}
		else{
			cout<<n<<" is not Prime number"<<endl;
		}
	}
	
	return 0;
}