import json

with open('moons.json') as moon_file:
    moons = json.load(moon_file)['results']
    moon_file.close()


def get_all_moons(min : int, max : int, prerequisite : int) -> list:
    output = []
    i = min
    while i < max:
        if (moons[i]["moonPrerequisites"] is None or moons[i]["moonPrerequisites"][0]["id"] <= prerequisite) and (
                    moons[i]["moonTypes"] is None or moons[i]["moonTypes"][0]["name"] != "Warp Painting") and (
                    moons[i]["isPostGame"] is not True) and (moons[i]["requiresRevisit"] is not True) and (
                    moons[i]["isStoryMoon"] is not True) and (moons[i]["moonTypes"] is None or (
                    moons[i]["moonTypes"][0]["name"] != "Hint Art" and moons[i]["moonTypes"][0]["name"] != "Tourist")):
            output.append({"name": moons[i]['name'], "id": moons[i]['id']})
        i += 1
    return output


def get_moon_json() -> list:
    output = []
    output.append({"set": "Cascade|1", "moons": get_all_moons(135, 174, 137), "transition_moon": None})
    output.append({"set": "Sand|1", "moons": get_all_moons(175, 263, 0), "transition_moon": moons[177]['name']})
    output.append({"set": "Sand|2", "moons": get_all_moons(175, 263, 178), "transition_moon": moons[178]['name']})
    output.append({"set": "Sand|3", "moons": get_all_moons(175, 263, 179), "transition_moon": None})
    output.append({"set": "Lake|1", "moons": get_all_moons(264, 305, 0), "transition_moon": moons[264]['name']})
    output.append({"set": "Lake|2", "moons": get_all_moons(264, 305, 265), "transition_moon": None})
    output.append({"set": "Wooded|1", "moons": get_all_moons(306, 381, 0), "transition_moon": moons[307]['name']})
    output.append({"set": "Wooded|2", "moons": get_all_moons(306, 381, 308), "transition_moon": moons[309]['name']})
    output.append({"set": "Wooded|3", "moons": get_all_moons(306, 381, 310), "transition_moon": None})
    output.append({"set": "Lost|1", "moons": get_all_moons(391, 425, 0), "transition_moon": None})
    output.append({"set": "Metro|1", "moons": get_all_moons(391, 425, 427), "transition_moon": moons[432]['name']})
    output.append({"set": "Metro|2", "moons": get_all_moons(391, 425, 433), "transition_moon": None})
    output.append({"set": "Snow|1", "moons": get_all_moons(507, 561, 0), "transition_moon": moons[511]['name']})
    output.append({"set": "Snow|2", "moons": get_all_moons(507, 561, 512), "transition_moon": None})
    output.append({"set": "Seaside|1", "moons": get_all_moons(562, 632, 0), "transition_moon": moons[566]['name']})
    output.append({"set": "Seaside|2", "moons": get_all_moons(562, 632, 567), "transition_moon": None})
    output.append({"set": "Luncheon|1", "moons": get_all_moons(633, 700, 634), "transition_moon": moons[635]['name']})
    output.append({"set": "Luncheon|2", "moons": get_all_moons(633, 700, 636), "transition_moon": moons[637]['name']})
    output.append({"set": "Luncheon|3", "moons": get_all_moons(633, 700, 638), "transition_moon": None})
    output.append({"set": "Bowsers|1", "moons": get_all_moons(711, 772, 715), "transition_moon": None})
    return output
