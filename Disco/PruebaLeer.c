#include <stdio.h>
#include <stdlib.h>
int main(){
	FILE *fptr;
	fptr = fopen("filename.txt", "w");
int i;

	for (i = 0; i < 5; i++) {
  		fprintf(fptr,"%d\n",i);
	}
	fclose(fptr);
	fptr = fopen("filename.txt", "r");


	char myLine[200];

	while(fgets(myLine,200,fptr)) {

	printf("%d\n",atoi(myLine));
}


// Close the file
	fclose(fptr);
return 0; 
}








