#include<bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
   int t;

   while(1) {
      t = a%b;
      if(t == 0)
         return b;
      a = b;
      b = t;
   }
}

int main()
{
   double p = 11, q = 23, n, track, e, z;

   n = p*q;
   z = (p-1)*(q-1);
   e = 5;

   while(e < z)
   {
      track = gcd(e, z);

      if(track == 1)
         break;
      else
         e++;
   }

   double d1, d, message, c, m;

   d1 = 1/e;
   d = fmod(d1,z);

   message = 12;

   c = pow(message,e);
   m = pow(c,d);

   c = fmod(c,n);
   m = fmod(m,n);
   
   cout << "Original Message = " << message << endl
        << "Encrypted message = " << c << endl
        << "Decrypted message = " << m << endl;

   return 0;
}