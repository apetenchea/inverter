# inverter
A script for obtaining the inverse of simple, linear assembly sequences (containing no loops).

Python version: 3.4.2

*Usage*
```Bash
py inverter.py input.asm
```
.
*Example*

```Assembly
xor eax, 0x123
sub eax, 0xad
xchg ax, bx
inc eax
xchg al, bl
dec ebx
rol eax, 0x2
ror ebx, 0x3
add ebx, 0xff
```
<pre>
  | |
  | |
  \ /
</pre>

```Assembly
sub ebx, 0xff
rol ebx, 0x3
ror eax, 0x2
inc ebx
xchg al, bl
dec eax
xchg ax, bx
add eax, 0xad
xor eax, 0x123
```

*Coding standard*<br>
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
