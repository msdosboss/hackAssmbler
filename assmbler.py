import sys
import os.path

from parser import Parse
from parser import A_INSTRUCTION
from parser import C_INSTRUCTION
from parser import L_INSTRUCTION
from code import DEST_DICT
from code import COMP_DICT
from code import JUMP_DICT

if __name__ == "__main__":
    program_name = ""
    if(len(sys.argv) < 2):
        # fallback
        program_name = "memAccess.asm"
    else:
        program_name = sys.argv[1]
        if (not os.path.exist(program_name)):
            # fallback
            program_name = "memAccess.asm"

    parser = Parse(program_name)

    instructions = []
    while (parser.hasMoreLines() is True):
        parser.advance()
        if (parser.instruction_type == A_INSTRUCTION):
            symbol = parser.getSymbol()
            # convert dec str to bin str
            symbol = int(symbol)
            symbol = bin(symbol)
            # removing leading 0b
            symbol = symbol[2:]
            instruction_len = 16
            symbol = symbol.zfill(instruction_len)

            instructions.append(symbol)

        elif (parser.instruction_type == C_INSTRUCTION):
            comp = parser.getComp()
            dest = parser.getDest()
            jump = parser.getJump()

            instruction = "111"
            instruction += COMP_DICT[comp]

            if (dest is not None):
                instruction += DEST_DICT[dest]
            else:
                instruction += "000"

            if (jump is not None):
                instruction += JUMP_DICT[jump]
            else:
                instruction += "000"

            instructions.append(instruction)            

    print(instructions)

    with open('b.out', "w") as f:
        for instruction in instructions:
            f.write(instruction + '\n')


       
 
