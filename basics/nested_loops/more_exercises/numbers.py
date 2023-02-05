beginning = int(input())
end = int(input())

for i in range(beginning, end + 1):
    for j in range(beginning, end + 1):
        for k in range(beginning, end + 1):
            for l in range(beginning, end + 1):
                if i % 2 == 0:
                    if l % 2 != 0:
                        if i > l and (j + k) % 2 == 0:
                            print(f"{i}{j}{k}{l}", end=" ")
                        else:
                            continue
                    else:
                        continue
                else:
                    if l % 2 == 0:
                        if i > l and (j + k) % 2 == 0:
                            print(f"{i}{j}{k}{l}", end=" ")
                        else:
                            continue
                    else:
                        continue
