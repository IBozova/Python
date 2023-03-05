def get_artifact(material):
    if material == "fragments":
        return "Valanyr"
    elif material == "motes":
        return "Dragonwrath"
    else:
        return "Shadowmourne"


key_materials = ["shards", "motes", "fragments"]
materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
material_found = ""

while True:
    while_break = 0
    material_input = input()
    materials = material_input.split(" ")
    material_str_lower = [i.lower() for i in materials]

    for i in range(0, len(material_str_lower), 2):
        material = material_str_lower[i + 1]
        count_material = int(material_str_lower[i])
        material_in = materials_dict.get(material, False)
        if material_in is False:
            materials_dict[material] = count_material
        else:
            materials_dict[material] += count_material
        if material in key_materials and materials_dict[material] >= 250:
            materials_dict[material] -= 250
            while_break = 1
            material_found = material
            break

    if while_break == 1:
        break

print(f"{get_artifact(material_found)} obtained!")
for key, value in materials_dict.items():
    print(f"{key}: {value}")
