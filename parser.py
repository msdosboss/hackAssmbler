import sys
import os.path

# I don't know a better way of doing python const
# I miss #define
A_INSTRUCTION = 0
C_INSTRUCTION = 1
L_INSTRUCTION = 2


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

    def get_symbol(self) -> str:
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

            while (index < len(current_line) and current_line[index] != '/' and current_line[index] != ' '):
                symbol += current_line[index]
                index += 1

        else:
            print(f"{self.instruction_type} instruction type does not have a symbol")
            return None

        return symbol

    def get_dest(self) -> str:
        if (self.instruction_type == C_INSTRUCTION):
            dest = ""
        else:
            print(f"{self.instruction_type} instruction type does not have a dest")
            return None

    def get_comp(self) -> str:
        if (self.instruction_type == C_INSTRUCTION):
            dest = ""
        else:
            print(f"{self.instruction_type} instruction type does not have a comp")
            return None

    def get_jump(self) -> str:
        if (self.instruction_type == C_INSTRUCTION):
            dest = ""
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
        # print(parser.get_symbol())
