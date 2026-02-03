@32767
D=A
@black_val
M=D
@32767
D=A
@black_val
M=D+M
M=M+1

@SCREEN
D=A

@i
M=D
(LOOP)
@black_val
D=M
@i
A=M
M=D
@i
//increase index
M=M+1

@24575
D=A

@i
D=D-M
@END
D;JEQ
@LOOP
0;JMP

(END)
@END
0;JMP
