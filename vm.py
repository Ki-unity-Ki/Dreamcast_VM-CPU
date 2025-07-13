# dreamcast_vm.py
class CPU:
    def __init__(self, mem):
        self.mem = mem
        self.pc = 0
        self.regs = [0]*16

    def fetch(self):
        insn = self.mem[self.pc]
        self.pc += 1
        return insn

    def execute(self, insn):
        # Define VM opcodes: 0x00=NOP, 0x10=INC R0, 0x20=DEC R0, 0xFF=HALT
        if insn == 0x00:
            pass
        elif insn == 0x10:
            self.regs[0] = (self.regs[0] + 1) & 0xFF
        elif insn == 0x20:
            self.regs[0] = (self.regs[0] - 1) & 0xFF
        elif insn == 0xFF:
            return False
        return True

    def run(self):
        running = True
        while running:
            insn = self.fetch()
            running = self.execute(insn)
        print("Final R0:", self.regs[0])

def main():
    mem = [0x10]*5 + [0x20]*2 + [0xFF]
    cpu = CPU(mem)
    cpu.run()

if __name__ == "__main__":
    main()
