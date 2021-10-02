#include <stdio.h>
int main(){
FILE *f1, *f2; char c;

printf("File : a.txt")
f1 = open("a.txt", "r");
while((c = getc(f1)) != EOF)
    printf("%c", c);
fclose(f1);
printf("----- end of a.txt")
printf("Copy a.txt to b.txt")
f1 = open("a.txt", "r");
f2 = open("b.txt", "w");
while((c = getc(f1)) != EOF)
    fputc((int)c,f2);
fclose(f2);
fclose(f1);
printf("File: b.txt")
f1 = open("b.txt", "r");
while((c = getc(f1)) != EOF)
    printf("%c", c);
fclose(f1);
printf("----- end of b.txt)
return 0;
}