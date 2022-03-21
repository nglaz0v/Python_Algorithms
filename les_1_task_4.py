# Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят, и сколько между ними находится букв.

smb1 = input("smb1: ").lower()
smb2 = input("smb2: ").lower()
smb1_ord = ord(smb1)
smb2_ord = ord(smb2)
if (ord('a') <= smb1_ord <= ord('z')) and (ord('a') <= smb2_ord <= ord('z')):
    smb1_pos = smb1_ord - (ord('a') - 1)
    smb2_pos = smb2_ord - (ord('a') - 1)
    smb_dist = smb2_ord - smb1_ord - 1
    print(f"smb1 #: {smb1_pos}")
    print(f"smb2 #: {smb2_pos}")
    print(f"delta: {smb_dist}")
