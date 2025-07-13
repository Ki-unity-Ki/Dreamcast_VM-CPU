# Dreamcast VM Interpreter (Python)

This is a prototype for a virtual CPU intended to simulate a very simplified Dreamcast-like environment. It supports a few basic instructions and a simple memory map.

## Features

- Custom instruction set
- Register-based CPU
- Instruction interpreter loop

## Run
- In bash:
- python3 dreamcast_vm.py

## Instruction Set

- 0x00: NOP
- 0x10: INC R0
- 0x20: DEC R0
- 0xFF: HALT

## Future Work

- Expand to 16-register support
- Add memory access and I/O
- Integrate a debugger
