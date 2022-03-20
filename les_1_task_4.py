# Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят, и сколько между ними находится букв.

smb1 = input("smb1: ")[0].lower()
smb2 = input("smb2: ")[0].lower()
smb1_pos = ord(smb1) - (ord('a') - 1)
smb2_pos = ord(smb2) - (ord('a') - 1)
smb_dist = ord(smb2) - ord(smb1) - 1
print(f"smb1 #: {smb1_pos}")
print(f"smb2 #: {smb2_pos}")
print(f"delta: {smb_dist}")
