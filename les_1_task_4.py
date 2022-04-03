# -*- coding: utf-8 -*-
"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

print(__doc__)
smb1 = input("Буква 1: ").lower()
smb2 = input("Буква 2: ").lower()
smb1_ord = ord(smb1)
smb2_ord = ord(smb2)
if (ord('a') <= smb1_ord <= ord('z')) and (ord('a') <= smb2_ord <= ord('z')):
    smb1_pos = smb1_ord - (ord('a') - 1)
    smb2_pos = smb2_ord - (ord('a') - 1)
    smb_dist = abs(smb2_ord - smb1_ord) - 1
    print(f"Позиция буквы 1: {smb1_pos}")
    print(f"Позиция буквы 2: {smb2_pos}")
    print(f"Букв между ними: {smb_dist}")
else:
    print("Это не строчные буквы латинского алфавита")
