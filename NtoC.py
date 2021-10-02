s = [] #리스트 선언

f = open("test.n", "r")
for line in f:
    s.append(line) #test.n파일의 내용을 읽어와서 리스트에 넣기
f.close()

f2 = open("test.c", "w+")

f2.write("#include <stdio.h>\n")
f2.write("int main(){\n")
f2.write("FILE *f1, *f2; char c;\n\n")

#N언어는 3가지 명령으로 구성되어 있다.
#1) cat filename : filename의 내용을 화면에 출력한다.
#2) cat filename > filename2 : filename의 내용을 filename2로 카피한다.
#3) echo "아무내용" : 아무내용 부분과 newline을 화면에 출력한다.


for i in range(len(s)):
    if s[i].find("echo") == 0: #echo로 시작하는지 찾음
        f2.write("printf("+s[i][5:-1]+")\n") #3)에 해당, echo 뒷부분과 newline을 화면에 출력
    elif s[i].find("cat") == 0: #cat으로 시작하는지 찾음
        if " > " in s[i]: #(빈칸>빈칸)이 포함되는 cat인지 찾음, #2)에 해당, filename의 내용을 filename2로 카피한다.
            num = s[i].find(' > ')
            f2.write('f1 = open("'+s[i][4:num]+'", "r");\n') #위에 계산한 find를 기준으로 파일의 이름을 가져온다.
            f2.write('f2 = open("'+s[i][num+3:-1]+'", "w");\n') #위에 계산한 find를 기준으로 파일의 이름을 가져옴
            f2.write('while((c = getc(f1)) != EOF)\n    fputc((int)c,f2);\n')
            f2.write('fclose(f2);\nfclose(f1);\n')
        else: #1에 해당, filename의 내용을 화면에 출력한다.
            f2.write('f1 = open("'+s[i][4:-1]+'", "r");\n') #-1까지 하는 이유는 newline부분을 스킵하기 위함이다.
            f2.write('while((c = getc(f1)) != EOF)\n    printf("%c", c);\n')
            f2.write('fclose(f1);\n')

f2.write("return 0;\n}")
f2.close()
