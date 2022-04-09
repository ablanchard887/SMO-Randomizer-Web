import json
import random

with open('moons.json') as moon_file:
    moons = json.load(moon_file)['results']
    moon_file.close()

coin_moons = [217, 283, 329, 412, 453, 528, 598, 658, 740]
purple_moons = [228, 285, 342, 465, 466, 536, 537, 604, 660, 661, 742, 743]
deep_woods = list(range(334, 343))


def rand(min : int, max : int) -> int:
    return random.randint(min, max)


def randomize(min : int, max : int) -> str:
    value = rand(min, max)
    return moons[value]


def generatestory(min : int, max : int, collectedMoons : list) -> str:
    while True:
        value = rand(min, max)
        if moons[value]["id"] not in collectedMoons:
            collectedMoons.append(moons[value]["id"])
            return moons[value]["name"]


def generate(min : int, max : int, prerequisite : int, amount : int, collectedMoons : list) -> list:
    i = 0
    return_list = []
    while i < amount:
        x = randomize(min, max)
        """
        if str(x['id']) in overrideArray:
            if settings.getboolean('Overrides', str(x['id'])):
                if (x["moonPrerequisites"] is None or x["moonPrerequisites"][0]["id"] <= prerequisite) and (
                        x["id"] not in collectedMoons):
                    trait = ""
                    if x["id"] in coin_moons:
                        trait += " [100 Coins] "
                    if x["id"] in deep_woods:
                        trait += " [Deep Woods] "
                    if x["id"] in purple_moons:
                        trait += " [Outfit Moon] "
                    if x["id"] == 339:
                        trait += " [500 Coins] "
                    randomizer.write(x["name"] + trait + "\n")
                    htmlrandomizer.write(checkbox_generate(x["name"] + "<b>" + trait + "</b>"))
                    collectedMoons.append(x["id"])
                    i += 1
            else:
                collectedMoons.append(x["id"])
        """
        if (x["moonPrerequisites"] is None or x["moonPrerequisites"][0]["id"] <= prerequisite) and (
                x["moonTypes"] is None or x["moonTypes"][0]["name"] != "Warp Painting") and (
                x["isPostGame"] is not True) and (x["requiresRevisit"] is not True) and (
                x["isStoryMoon"] is not True) and (x["moonTypes"] is None or (
                x["moonTypes"][0]["name"] != "Hint Art" and x["moonTypes"][0]["name"] != "Tourist")) and (
                x["id"] not in collectedMoons):
            trait = ""
            if x["id"] in coin_moons:
                trait += " [100 Coins] "
            if x["id"] in deep_woods:
                trait += " [Deep Woods] "
            if x["id"] in purple_moons:
                trait += " [Outfit Moon] "
            if x["id"] == 339:
                trait += " [500 Coins] "
            return_list.append(x['name'])
            collectedMoons.append(x["id"])
            i += 1
    return return_list


def generate_page(seed : int, settings : dict) -> str:
    random.seed(seed)
    bowserSprinkle = True # Temp
    peaceSkips = True # Temp
    output = []
    collectedmoons = []

    # Cascade
    cascade_moon_list = [moons[135]["name"], moons[136]["name"]]

    output.append({"kingdom": "Cascade", "moons": cascade_moon_list + generate(135, 174, 137, 1, collectedmoons)})
    #

    # Sand
    moonCount = 0
    sand_moon_list = []

    local = rand(0, 16)
    moonCount += local

    sand_moon_list += generate(175, 263, 0, local, collectedmoons)
    if moonCount < 16:
        sand_moon_list.append(moons[175]["name"])
        moonCount += 1

        local = rand(0, 16 - moonCount)
        moonCount += local

        sand_moon_list += generate(175, 263, 176, local, collectedmoons)
    
    if not peaceSkips:
        if moonCount < 16:
            sand_moon_list.append(moons[176]["name"])
            moonCount += 1

            local = rand(0, 16 - moonCount)
            moonCount += local

            sand_moon_list += generate(175, 263, 177, local, collectedmoons)

            if moonCount < 14:
                sand_moon_list.append(moons[177]["name"])
                moonCount += 3

                local = rand(0, 16 - moonCount)
                moonCount += local

                sand_moon_list += generate(175, 263, 178, local, collectedmoons)

                if moonCount < 14:
                    sand_moon_list.append(moons[178]["name"])
                    moonCount += 3

                    sand_moon_list += generate(175, 263, 179, 16 - moonCount, collectedmoons)
                elif 16 > moonCount >= 14:
                    sand_moon_list += generate(175, 263, 177, 16 - moonCount, collectedmoons)

            elif 16 > moonCount >= 14:
                sand_moon_list += generate(175, 263, 177, 16 - moonCount, collectedmoons)
    else:
        if moonCount < 14:
            sand_moon_list.append(moons[177]["name"])
            moonCount += 3

            local = rand(0, 16 - moonCount)
            moonCount += local

            sand_moon_list += generate(175, 263, 178, local, collectedmoons)

            if moonCount < 14:
                sand_moon_list.append(moons[178]["name"])
                moonCount += 3

                sand_moon_list += generate(175, 263, 179, 16 - moonCount, collectedmoons)
            elif 16 > moonCount >= 14:
                sand_moon_list += generate(175, 263, 177, 16 - moonCount, collectedmoons)

        elif 16 > moonCount >= 14:
            sand_moon_list += generate(175, 263, 177, 16 - moonCount, collectedmoons)
    output.append({"kingdom": "Sand", "moons": sand_moon_list})
    #

    # Lake
    moonCount = 0
    lake_moon_list = []

    local = rand(0, 8)
    moonCount += local

    lake_moon_list += generate(264, 305, 0, local, collectedmoons)

    if moonCount < 6:
        lake_moon_list.append(moons[264]["name"])
        moonCount += 3

        lake_moon_list += generate(264, 305, 265, 8 - moonCount, collectedmoons)
    elif 8 > moonCount >= 6:
        lake_moon_list += generate(264, 305, 0, 8 - moonCount, collectedmoons)
    output.append({"kingdom": "Lake", "moons": lake_moon_list})
    #
    
    # Wooded
    moonCount = 0
    wooded_moon_list = []

    local = rand(0, 16)
    moonCount += local

    wooded_moon_list += generate(306, 381, 0, local, collectedmoons)

    if moonCount < 16:
        wooded_moon_list.append(moons[306]["name"])
        moonCount += 1

        local = rand(0, 16 - moonCount)
        moonCount += local

        wooded_moon_list += generate(306, 381, 307, local, collectedmoons)

        if moonCount < 14:
            wooded_moon_list.append(moons[307]["name"])
            moonCount += 3

            local = rand(0, 16 - moonCount)
            moonCount += local

            wooded_moon_list += generate(306, 381, 308, local, collectedmoons)

            if moonCount < 16:
                wooded_moon_list.append(moons[308]["name"])
                moonCount += 1

                local = rand(0, 16 - moonCount)
                moonCount += local

                wooded_moon_list += generate(306, 381, 309, local, collectedmoons)

                if moonCount < 14:
                    wooded_moon_list.append(moons[309]["name"])
                    moonCount += 3

                    wooded_moon_list += generate(306, 381, 310, 16 - moonCount, collectedmoons)
                elif 16 > moonCount >= 14:
                    wooded_moon_list += generate(306, 381, 309, 16 - moonCount, collectedmoons)
        elif 16 > moonCount >= 14:
            wooded_moon_list += generate(306, 381, 307, 16 - moonCount, collectedmoons)
    output.append({"kingdom": "Wooded", "moons": wooded_moon_list})
    #

    # Lost
    output.append({"kingdom": "Lost", "moons": generate(391, 425, 0, 10, collectedmoons)})
    #

    # Metro
    moonCount = 3
    metro_moon_list = [moons[426]["name"]]

    local = rand(0, 20 - moonCount)
    moonCount += local

    generate(426, 506, 427, local, collectedmoons)

    if moonCount < 20:
        metro_moon_list.append(generatestory(427, 430, collectedmoons))
        moonCount += 1

        local = rand(0, 20 - moonCount)
        moonCount += local

        metro_moon_list += generate(426, 506, 427, local, collectedmoons)

        if moonCount < 20:
            story = generatestory(427, 430, collectedmoons)
            metro_moon_list.append(story)
            moonCount += 1

            local = rand(0, 20 - moonCount)
            moonCount += local

            metro_moon_list += generate(426, 506, 427, local, collectedmoons)

            if moonCount < 20:
                story = generatestory(427, 430, collectedmoons)
                metro_moon_list.append(story)
                moonCount += 1

                local = rand(0, 20 - moonCount)
                moonCount += local

                metro_moon_list += generate(426, 506, 427, local, collectedmoons)

                if moonCount < 20:
                    story = generatestory(427, 430, collectedmoons)
                    metro_moon_list.append(story)
                    moonCount += 1

                    local = rand(0, 20 - moonCount)
                    moonCount += local

                    metro_moon_list += generate(426, 506, 428, local, collectedmoons)

                    if moonCount < 20:
                        metro_moon_list.append(moons[431]["name"])
                        moonCount += 1

                        local = rand(0, 20 - moonCount)
                        moonCount += local

                        metro_moon_list += generate(426, 506, 432, local, collectedmoons)

                        if moonCount < 18:
                            metro_moon_list.append(moons[432]["name"])
                            moonCount += 3

                            metro_moon_list += generate(426, 506, 433, 20 - moonCount, collectedmoons)
                        elif 20 > moonCount >= 18:
                            metro_moon_list += generate(426, 506, 432, 20 - moonCount, collectedmoons)
    output.append({"kingdom": "Metro", "moons": metro_moon_list})
    #

    # Snow
    moonCount = 0
    snow_moon_list = []

    local = rand(0, 10)
    moonCount += local

    snow_moon_list += generate(507, 561, 0, local, collectedmoons)

    if not peaceSkips:
        if moonCount < 10:
            story = generatestory(507, 510, collectedmoons)
            snow_moon_list.append(story)
            moonCount += 1

            local = rand(0, 10 - moonCount)
            moonCount += local

            snow_moon_list += generate(507, 561, 0, local, collectedmoons)

            if moonCount < 10:
                story = generatestory(507, 510, collectedmoons)
                snow_moon_list.append(story)
                moonCount += 1

                local = rand(0, 10 - moonCount)
                moonCount += local

                snow_moon_list += generate(507, 561, 0, local, collectedmoons)

                if moonCount < 10:
                    story = generatestory(507, 510, collectedmoons)
                    snow_moon_list.append(story)
                    moonCount += 1

                    local = rand(0, 10 - moonCount)
                    moonCount += local

                    snow_moon_list += generate(507, 561, 0, local, collectedmoons)

                    if moonCount < 10:
                        story = generatestory(507, 510, collectedmoons)
                        snow_moon_list.append(story)
                        moonCount += 1

                        local = rand(0, 10 - moonCount)
                        moonCount += local

                        snow_moon_list += generate(507, 561, 0, local, collectedmoons)

                        if moonCount < 8:
                            snow_moon_list.append(moons[511]["name"])
                            moonCount += 3

                            snow_moon_list += generate(507, 561, 512, 10 - moonCount, collectedmoons)
                        elif 10 > moonCount >= 8:
                            snow_moon_list += generate(507, 561, 0, 10 - moonCount, collectedmoons)
    else:
        if moonCount < 8:
            snow_moon_list.append(moons[511]["name"])
            moonCount += 3

            snow_moon_list += generate(507, 561, 512, 10 - moonCount, collectedmoons)
        elif 10 > moonCount >= 8:
            snow_moon_list += generate(507, 561, 0, 10 - moonCount, collectedmoons)
    output.append({"kingdom": "Snow", "moons": snow_moon_list})
    #
    
    # Seaside
    moonCount = 0
    seaside_moon_list = []

    local = rand(0, 10)
    moonCount += local

    seaside_moon_list += generate(562, 632, 0, local, collectedmoons)

    if moonCount < 10:
        story = generatestory(562, 565, collectedmoons)
        seaside_moon_list.append(story)
        moonCount += 1

        local = rand(0, 10 - moonCount)
        moonCount += local

        seaside_moon_list += generate(562, 632, 0, local, collectedmoons)

        if moonCount < 10:
            story = generatestory(562, 565, collectedmoons)
            seaside_moon_list.append(story)
            moonCount += 1

            local = rand(0, 10 - moonCount)
            moonCount += local

            seaside_moon_list += generate(562, 632, 0, local, collectedmoons)

            if moonCount < 10:
                story = generatestory(562, 565, collectedmoons)
                seaside_moon_list.append(story)
                moonCount += 1

                local = rand(0, 10 - moonCount)
                moonCount += local

                seaside_moon_list += generate(562, 632, 0, local, collectedmoons)

                if moonCount < 10:
                    story = generatestory(562, 565, collectedmoons)
                    seaside_moon_list.append(story)
                    moonCount += 1

                    local = rand(0, 10 - moonCount)
                    moonCount += local

                    seaside_moon_list += generate(562, 632, 0, local, collectedmoons)

                    if moonCount < 8:
                        seaside_moon_list.append(moons[566]["name"])
                        moonCount += 3

                        seaside_moon_list += generate(562, 632, 567, 10 - moonCount, collectedmoons)
                    elif 10 > moonCount >= 8:
                        seaside_moon_list += generate(562, 632, 0, 10 - moonCount, collectedmoons)
    output.append({"kingdom": "Seaside", "moons": seaside_moon_list})
    #

    # Luncheon
    moonCount = 1
    luncheon_moon_list = [moons[633]["name"]]

    local = rand(0, 15)
    moonCount += local

    luncheon_moon_list += generate(633, 700, 634, local, collectedmoons)

    if moonCount < 18:
        luncheon_moon_list.append(moons[634]["name"])
        moonCount += 1

        local = rand(0, 18 - moonCount)
        moonCount += local

        luncheon_moon_list += generate(633, 700, 635, local, collectedmoons)

        if moonCount < 16:
            luncheon_moon_list.append(moons[635]["name"])
            moonCount += 3

            local = rand(0, 18 - moonCount)
            moonCount += local

            luncheon_moon_list += generate(633, 700, 636, local, collectedmoons)

            if moonCount < 18:
                luncheon_moon_list.append(moons[636]["name"])
                moonCount += 1

                local = rand(0, 18 - moonCount)
                moonCount += local

                luncheon_moon_list += generate(633, 700, 637, local, collectedmoons)

                if moonCount < 16:
                    luncheon_moon_list.append(moons[637]["name"])
                    moonCount += 3

                    luncheon_moon_list += generate(633, 700, 638, 18 - moonCount, collectedmoons)

                elif 18 > moonCount >= 16:
                    luncheon_moon_list += generate(633, 700, 637, 18 - moonCount, collectedmoons)
        elif 18 > moonCount >= 16:
            luncheon_moon_list += generate(633, 700, 635, 18 - moonCount, collectedmoons)
    output.append({"kingdom": "Luncheon", "moons": luncheon_moon_list})
    #

    # Bowsers
    moonCount = 6
    bowsers_moon_list = [moons[711]["name"], moons[712]["name"], moons[713]["name"], moons[714]["name"]]
    sprinkleID = 715

    if bowserSprinkle:
        sprinkleID = 714

    bowsers_moon_list += generate(711, 772, sprinkleID, 8 - moonCount, collectedmoons)
    output.append({"kingdom": "Bowser's", "moons": bowsers_moon_list})
    #

    return output