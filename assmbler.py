import sys
import os.path

from parser import Parse
from parser import A_INSTRUCTION
from parser import C_INSTRUCTION
from parser import L_INSTRUCTION
from code import DEST_DICT
from code import COMP_DICT
from code import JUMP_DICT
from symbolTable import SymbolTable


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
    symbol_table = SymbolTable()

    instructions = []
    instruction_count = -1
    new_variable_address = 16
    while (parser.hasMoreLines() is True):
        instruction_count += 1
        parser.advance()
        if (parser.instruction_type == A_INSTRUCTION):
            symbol = parser.getSymbol()
            # convert dec str to bin str
            try:
                symbol_int = int(symbol)
                symbol = bin(symbol_int)

            # this exception is for symbols (meaning none consts numbers)
            except ValueError:
                if (symbol_table.contains(symbol)):
                    address = symbol_table.getAddress(symbol)
                    symbol = bin(address)

                else:
                    symbol_table.addEntry(symbol, new_variable_address)
                    symbol = bin(new_variable_address)
                    new_variable_address += 1
            
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

            if (dest is None):
                instruction += "000"
            else:
                instruction += DEST_DICT[dest]

            if (jump is None):
                instruction += "000"
            else:
                instruction += JUMP_DICT[jump]

            instructions.append(instruction)            

        # L_INSTRUCTION
        else:
            symbol = parser.getSymbol()
            symbol_table.addEntry(symbol, instruction_count)
            # L_INSTRUCTIONS don't exist in the machine language so I do not want to count for instruction_count
            instruction_count -= 1
            

    print(instructions)

    with open('b.out', "w") as f:
        for instruction in instructions:
            f.write(instruction + '\n')


       
 
