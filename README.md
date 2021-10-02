#NtoC-translator-

3가지 명령으로만 구성된 N이라는 가상의 언어가 있다고 가정하고 이를 C언어로 변환시키는 번역기입니다.
아래는 해당 3가지 명령어 입니다.
  1. cat filename : 해당 filename의 내용을 화면에 출력한다.
  2. cat filename1 > filename2 : filename1의 내용을 filename2로 카피한다.
  3. echo "아무내용" : 아무내용 부분과 newline을 화면에 출력한다.

***

N언어 파일의 내용    
  echo "File : a.txt"    
  cat a.txt    
  echo "----- end of a.txt"    
  echo "Copy a.txt to b.txt"    
  cat a.txt > b.txt    
  echo "File: b.txt"    
  cat b.txt    
  echo "----- end of b.txt"    
    
***
    
C언어 파일의 내용    
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
