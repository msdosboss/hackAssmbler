// D = 17
(ORCA)
@17
D=A // Testing inline comment with = ; 

//RAM[100] = 17
@100
M=D
@i
@ORCA
@j
@ORCATWO
//RAM[100] = RAM[200]
@200
(ORCATWO)
D=M
@100
M=D
M = D; JMP
