import sys
import os.path

# I don't know a better way of doing python const
# I miss #define
A_INSTRUCTION = 0
C_INSTRUCTION = 1
L_INSTRUCTION = 2

VALID_DEST = [
    "M",
    "D",
    "DM",
    "A",
    "AM",
    "AD",
    "ADM"
]

VALID_COMP = [
    "0",
    "1",
    "-1",
    "D",
    "A",
    "!D",
    "!A",
    "-D",
    "-A",
    "D+1",
    "A+1",
    "D-1",
    "A-1",
    "D+A",
    "D-A",
    "A-D",
    "D&A",
    "D|A",
    "M",
    "!M",
    "-M",
    "M+1",
    "M-1",
    "D+M",
    "D-M",
    "M-D",
    "D&M",
    "D|M"
]

VALID_JUMP = [
    "JGT",
    "JEQ",
    "JGE",
    "JLT",
    "JNE",
    "JLE",
    "JMP"
]

class Parse:
    def __init__(self, program_name: str):
        file = open(program_name, "r")
        self.lines_list = file.readlines()
        file.close()
        self.index = -1
        self.instruction_type = None

    def hasMoreLines(self) -> bool:
        if (self.index + 1 >= len(self.lines_list)):
            return False
        return True

    # Count is how many instructions you want to advance through
    def advance(self, count: int = 1) -> None:
        for i in range(count):

            while (self.hasMoreLines()):
                self.index += 1
                current_line = self.lines_list[self.index]
                # skipping comments and blank lines
                # This is a bit fragile 
                if(current_line[0] == '\n' or current_line[0] == '/'):
                    continue
                else:
                    # means we are at the end of the count
                    if (i + 1 == count):
                        self.lines_list[self.index] = self.lines_list[self.index].replace(" ", "")
                        self.lines_list[self.index] = self.lines_list[self.index].replace("\n", "")
                        # removes inline comments if they exist
                        comment_index = self.lines_list[self.index].find('/')
                        if (comment_index != -1):
                            self.lines_list[self.index] = self.lines_list[self.index][:comment_index]
                        # declaring what type of instruction is on this line
                        # also this is pretty fragile
                        # I should make it better
                        if (current_line[0] == '@'):
                            self.instruction_type = A_INSTRUCTION
                        elif (current_line[0] == '('):
                            self.instruction_type = L_INSTRUCTION
                        else:
                            self.instruction_type = C_INSTRUCTION

                        return current_line
                    else:
                        continue

            # MegaMind meme goes here
            print("No lines?")
            return None

    def getSymbol(self) -> str:
        current_line = self.lines_list[self.index]
        index = 0
        symbol = ""
        if (self.instruction_type == L_INSTRUCTION):
            while (current_line[index] != '('):
                index += 1
            index += 1

            while (current_line[index] != ')'):
                symbol += current_line[index]
                index += 1


        elif (self.instruction_type == A_INSTRUCTION):
            while (current_line[index] != '@'):
                index += 1
            index += 1

            while (index < len(current_line)):
                symbol += current_line[index]
                index += 1

        else:
            print(f"{self.instruction_type} instruction type does not have a symbol")
            return None

        return symbol

    def getDest(self) -> str:
        if (self.instruction_type == C_INSTRUCTION):
            current_line = self.lines_list[self.index]
            if ('=' in current_line):
                dest = ""
                index = 0

                while (current_line[index] != '='):
                    dest += current_line[index]
                    index += 1

                if (dest in VALID_DEST):
                    return dest
                else:
                    print(f"{dest} is not a valid dest")
                    return None
            else:
                return None
        else:
            print(f"{self.instruction_type} instruction type does not have a dest")
            return None

    def getComp(self) -> str:
        if (self.instruction_type == C_INSTRUCTION):
            comp = ""
            current_line = self.lines_list[self.index]
            index =  0
            if ('=' in current_line):
                # iterating past the dest
                while (current_line[index] != '='):
                    index += 1
                index += 1

            while(index < len(current_line) and current_line[index] != ';'):
                comp += current_line[index]
                index += 1

            if (comp in VALID_COMP):
                return comp
            else:
                print(f"{comp} is not a valid comp")
                return None
        else:
            print(f"{self.instruction_type} instruction type does not have a comp")
            return None

    def getJump(self) -> str:
        if (self.instruction_type == C_INSTRUCTION):
            jump = ""
            current_line = self.lines_list[self.index]
            if (';' in current_line):
                index = 0
                # moving the index onto the jmp instruction
                while (current_line[index] != ';'):
                    index += 1
                index += 1

                while (index < len(current_line)):
                    jump += current_line[index]
                    index += 1

                if (jump in VALID_JUMP):
                    return jump
                else:
                    print(f"{jump} is not a valid jump")
                    return None
            else:
                return None
        else:
            print(f"{self.instruction_type} instruction type does not have a jump")
            return None

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
    while (parser.advance() != None):
        print(parser.lines_list[parser.index])
        # print(parser.getDest())
        # print(parser.getSymbol())
        # print(parser.getComp())
        print(parser.getJump())
