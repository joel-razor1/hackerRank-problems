#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>




   int main(){

       int ar[6][6], sum[20],i,j,count=0,largest;

       for(i=0;i<6;i++){
           for(j=0;j<6;j++){
               scanf("%d",&ar[i][j]);
           }
       }

       for(i=0;i<4;i++){
           for(j=0;j<4;j++){
             sum[count++] =ar[i][j]+ar[i][j+1]+ar[i][j+2]+ar[i+1][j+1]+ar[i+2][j]+ar[i+2][j+1]+ar[i+2][j+2];
           }
       }
        largest=sum[0];
        for(i=1;i<count;i++){
            if(largest<sum[i]){
                largest=sum[i];
            }
    
        }
        printf("%d",largest);

       return 0;
   }

