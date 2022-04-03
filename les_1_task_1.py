# -*- coding: utf-8 -*-
"""
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

print(__doc__)
op__5_and_6 = 5 & 6
op__5_or_6 = 5 | 6
op__5_xor_6 = 5 ^ 6
op__5_shr_2 = 5 >> 2
op__5_shl_2 = 5 << 2
print(f"5 and 6 = {op__5_and_6} \t{bin(5)} and {bin(6)} = {bin(op__5_and_6)}")
print(f"5  or 6 = {op__5_or_6} \t{bin(5)}  or {bin(6)} = {bin(op__5_or_6)}")
print(f"5 xor 6 = {op__5_xor_6} \t{bin(5)} xor {bin(6)} = {bin(op__5_xor_6)}")
print(f"5 shr 2 = {op__5_shr_2} \t{bin(5)} shr {bin(2)} = {bin(op__5_shr_2)}")
print(f"5 shl 2 = {op__5_shl_2}\t{bin(5)} shl {bin(2)} = {bin(op__5_shl_2)}")
