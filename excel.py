import openpyxl
wb = openpyxl.reader.excel.load_workbook(filename="sample_data.xlsx")
wb.active = 0
sheet = wb.active

def calculation_courier(distance, city):
    if city == 'Алматы':
        poda4a = sheet['D5'].value
        if distance <= 2:
            final = int(poda4a)
        else:
            final = int(poda4a) + (distance - 2) * sheet['H5'].value

    elif city == 'Нур-Султан':
        poda4a = sheet['D6'].value
        if distance <= 2:
            final = int(poda4a)
        elif distance > 10:
            final = int(poda4a) + 8 * 119 + (distance - 10) * 134
        else:
            final = int(poda4a) + (distance - 2) * 119

    else:
        final = "В этом городе массфикс курьера нет!"

    return final


# экспресс

def calculation_express(distance, city, time_str):
    if city == sheet['B7'].value:
        poda4a = sheet['D7'].value
        time = int(time_str)
        if distance <= sheet['F7'].value:
            if time <= sheet['E7'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E7'].value) * sheet['G7'].value
        else:
            if time <= sheet['E7'].value:
                final = int(poda4a) + (distance - sheet['F7'].value) * sheet['H7'].value
            else:
                final = int(poda4a) + (distance - sheet['F7'].value) * sheet['H7'].value + (time - sheet['E7'].value) * sheet['G7'].value

    elif city == sheet['B8'].value:
        poda4a = sheet['D8'].value
        time = int(time_str)
        if distance <= sheet['F8'].value:
            if time <= sheet['E8'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E8'].value) * sheet['G8'].value
        else:
            if time <= sheet['E8'].value:
                final = int(poda4a) + (distance - sheet['F8'].value) * sheet['H8'].value
            else:
                final = int(poda4a) + (distance - sheet['F8'].value) * sheet['H8'].value + (time - sheet['E8'].value) * sheet['G8'].value

    elif city == city == sheet['B9'].value:
        poda4a = sheet['D9'].value
        time = int(time_str)
        if distance <= sheet['F9'].value:
            if time <= sheet['E9'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E9'].value) * sheet['G9'].value
        else:
            if time <= sheet['E9'].value:
                final = int(poda4a) + (distance - sheet['F9'].value) * sheet['H9'].value
            else:
                final = int(poda4a) + (distance - sheet['F9'].value) * sheet['H9'].value + (time - sheet['E9'].value) * sheet['G9'].value

    elif city == sheet['B10'].value:
        poda4a = sheet['D10'].value
        time = int(time_str)
        if distance <= sheet['F10'].value:
            if time <= sheet['E10'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E10'].value) * sheet['G10'].value
        else:
            if time <= sheet['E10'].value:
                final = int(poda4a) + (distance - sheet['F10'].value) * sheet['H10'].value
            else:
                final = int(poda4a) + (distance - sheet['F10'].value) * sheet['H10'].value + (time - sheet['E10'].value) * sheet['G10'].value

    elif city == sheet['B11'].value:
        poda4a = sheet['D11'].value
        time = int(time_str)
        if distance <= sheet['F11'].value:
            if time <= sheet['E11'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E11'].value) * sheet['G11'].value
        else:
            if time <= sheet['E11'].value:
                final = int(poda4a) + (distance - sheet['F11'].value) * sheet['H11'].value
            else:
                final = int(poda4a) + (distance - sheet['F11'].value) * sheet['H11'].value + (time - sheet['E11'].value) * sheet['G11'].value

    elif city == sheet['B12'].value:
        poda4a = sheet['D12'].value
        time = int(time_str)
        if distance <= sheet['F12'].value:
            if time <= sheet['E12'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E12'].value) * sheet['G12'].value
        else:
            if time <= sheet['E12'].value:
                final = int(poda4a) + (distance - sheet['F12'].value) * sheet['H12'].value
            else:
                final = int(poda4a) + (distance - sheet['F12'].value) * sheet['H12'].value + (
                            time - sheet['E12'].value) * sheet['G12'].value

    elif city == sheet['B13'].value:
        poda4a = sheet['D13'].value
        time = int(time_str)
        if distance <= sheet['F13'].value:
            if time <= sheet['E13'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E13'].value) * sheet['G13'].value
        else:
            if time <= sheet['E13'].value:
                final = int(poda4a) + (distance - sheet['F13'].value) * sheet['H13'].value
            else:
                final = int(poda4a) + (distance - sheet['F13'].value) * sheet['H13'].value + (
                            time - sheet['E13'].value) * sheet['G13'].value

    elif city == sheet['B14'].value:
        poda4a = sheet['D14'].value
        time = int(time_str)
        if distance <= sheet['F14'].value:
            if time <= sheet['E14'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E14'].value) * sheet['G14'].value
        else:
            if time <= sheet['E14'].value:
                final = int(poda4a) + (distance - sheet['F14'].value) * sheet['H14'].value
            else:
                final = int(poda4a) + (distance - sheet['F14'].value) * sheet['H14'].value + (
                            time - sheet['E14'].value) * sheet['G14'].value

    elif city == sheet['B15'].value:
        poda4a = sheet['D15'].value
        time = int(time_str)
        if distance <= sheet['F15'].value:
            if time <= sheet['E15'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E15'].value) * sheet['G15'].value
        else:
            if time <= sheet['E15'].value:
                final = int(poda4a) + (distance - sheet['F15'].value) * sheet['H15'].value
            else:
                final = int(poda4a) + (distance - sheet['F15'].value) * sheet['H15'].value + (
                            time - sheet['E15'].value) * sheet['G15'].value

    elif city == sheet['B16'].value:
        poda4a = sheet['D16'].value
        time = int(time_str)
        if distance <= sheet['F16'].value:
            if time <= sheet['E16'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E16'].value) * sheet['G16'].value
        else:
            if time <= sheet['E16'].value:
                final = int(poda4a) + (distance - sheet['F16'].value) * sheet['H16'].value
            else:
                final = int(poda4a) + (distance - sheet['F16'].value) * sheet['H16'].value + (
                            time - sheet['E16'].value) * sheet['G16'].value

    elif city == sheet['B17'].value:
        poda4a = sheet['D17'].value
        time = int(time_str)
        if distance <= sheet['F17'].value:
            if time <= sheet['E17'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E17'].value) * sheet['G17'].value
        else:
            if time <= sheet['E17'].value:
                final = int(poda4a) + (distance - sheet['F17'].value) * sheet['H17'].value
            else:
                final = int(poda4a) + (distance - sheet['F17'].value) * sheet['H17'].value + (
                            time - sheet['E17'].value) * sheet['G17'].value

    elif city == sheet['B18'].value:
        poda4a = sheet['D18'].value
        time = int(time_str)
        if distance <= sheet['F18'].value:
            if time <= sheet['E18'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E18'].value) * sheet['G18'].value
        else:
            if time <= sheet['E18'].value:
                final = int(poda4a) + (distance - sheet['F18'].value) * sheet['H18'].value
            else:
                final = int(poda4a) + (distance - sheet['F18'].value) * sheet['H18'].value + (
                            time - sheet['E18'].value) * sheet['G18'].value

    elif city == sheet['B19'].value:
        poda4a = sheet['D19'].value
        time = int(time_str)
        if distance <= sheet['F19'].value:
            if time <= sheet['E19'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E19'].value) * sheet['G19'].value
        else:
            if time <= sheet['E19'].value:
                final = int(poda4a) + (distance - sheet['F19'].value) * sheet['H19'].value
            else:
                final = int(poda4a) + (distance - sheet['F19'].value) * sheet['H19'].value + (
                            time - sheet['E19'].value) * sheet['G19'].value

    elif city == sheet['B20'].value:
        poda4a = sheet['D20'].value
        time = int(time_str)
        if distance <= sheet['F20'].value:
            if time <= sheet['E20'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E20'].value) * sheet['G20'].value
        else:
            if time <= sheet['E20'].value:
                final = int(poda4a) + (distance - sheet['F20'].value) * sheet['H20'].value
            else:
                final = int(poda4a) + (distance - sheet['F20'].value) * sheet['H20'].value + (
                            time - sheet['E20'].value) * sheet['G20'].value

    elif city == sheet['B21'].value:
        poda4a = sheet['D21'].value
        time = int(time_str)
        if distance <= sheet['F21'].value:
            if time <= sheet['E21'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E21'].value) * sheet['G21'].value
        else:
            if time <= sheet['E21'].value:
                final = int(poda4a) + (distance - sheet['F21'].value) * sheet['H21'].value
            else:
                final = int(poda4a) + (distance - sheet['F21'].value) * sheet['H21'].value + (
                            time - sheet['E21'].value) * sheet['G21'].value

    elif city == sheet['B22'].value:
        poda4a = sheet['D22'].value
        time = int(time_str)
        if distance <= sheet['F22'].value:
            if time <= sheet['E22'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E22'].value) * sheet['G22'].value
        else:
            if time <= sheet['E22'].value:
                final = int(poda4a) + (distance - sheet['F22'].value) * sheet['H22'].value
            else:
                final = int(poda4a) + (distance - sheet['F22'].value) * sheet['H22'].value + (
                            time - sheet['E22'].value) * sheet['G22'].value

    elif city == sheet['B23'].value:
        poda4a = sheet['D23'].value
        time = int(time_str)
        if distance <= sheet['F23'].value:
            if time <= sheet['E23'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E23'].value) * sheet['G23'].value
        else:
            if time <= sheet['E23'].value:
                final = int(poda4a) + (distance - sheet['F23'].value) * sheet['H23'].value
            else:
                final = int(poda4a) + (distance - sheet['F23'].value) * sheet['H23'].value + (
                            time - sheet['E23'].value) * sheet['G23'].value

    elif city == sheet['B24'].value:
        poda4a = sheet['D24'].value
        time = int(time_str)
        if distance <= sheet['F24'].value:
            if time <= sheet['E24'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E24'].value) * sheet['G24'].value
        else:
            if time <= sheet['E24'].value:
                final = int(poda4a) + (distance - sheet['F24'].value) * sheet['H24'].value
            else:
                final = int(poda4a) + (distance - sheet['F24'].value) * sheet['H24'].value + (
                            time - sheet['E24'].value) * sheet['G24'].value

    elif city == sheet['B25'].value:

        poda4a = sheet['D25'].value

        time = int(time_str)

        if distance <= sheet['F25'].value:

            if time <= sheet['E25'].value:

                final = int(poda4a)

            else:

                final = int(poda4a) + (time - sheet['E25'].value) * sheet['G25'].value

        else:

            if time <= sheet['E25'].value:

                final = int(poda4a) + (distance - sheet['F25'].value) * sheet['H25'].value

            else:

                final = int(poda4a) + (distance - sheet['F25'].value) * sheet['H25'].value + (
                            time - sheet['E25'].value) * sheet['G25'].value

    elif city == sheet['B26'].value:
        poda4a = sheet['D26'].value
        time = int(time_str)
        if distance <= sheet['F26'].value:
            if time <= sheet['E26'].value:
                final = int(poda4a)
            else:
                final = int(poda4a) + (time - sheet['E26'].value) * sheet['G26'].value
        else:
            if time <= sheet['E26'].value:
                final = int(poda4a) + (distance - sheet['F26'].value) * sheet['H26'].value
            else:
                final = int(poda4a) + (distance - sheet['F26'].value) * sheet['H26'].value + (
                            time - sheet['E26'].value) * sheet['G26'].value

    else:
        final = "В этом городе нет массфикс доставки!"
    return final


#### Created by Salikh Pernebek ####