# Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят, и сколько между ними находится букв.

smb1 = input("smb1: ").lower()
smb2 = input("smb2: ").lower()
print(f"#smb1: {ord(smb1) - (ord('a') - 1)}")
print(f"#smb2: {ord(smb2) - (ord('a') - 1)}")
print(f"between: {ord(smb2) - ord(smb1) - 1}")
