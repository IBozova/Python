version_sw = input().split(".")

str_sw = ""

for item in version_sw:
    str_sw += item

int_sw = int(str_sw)

if int_sw >= 900:
    print("8.9.9")
else:
    new_ver = int_sw + 1
    new_ver_str = str(new_ver)
    new_ver_list = list(new_ver_str)
    print(f"{new_ver_list[0]}.{new_ver_list[1]}.{new_ver_list[2]}")
