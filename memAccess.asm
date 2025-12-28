// D = 17
@17
D=A // Testing inline comment with = ; 

//RAM[100] = 17
@100
M=D

//RAM[100] = RAM[200]
@200
D=M
@100
M=D
M = D; JMP
