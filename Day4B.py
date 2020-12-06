import re

def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def list_combine(inputlist):
    """Will take a list with blanks and multiple lines, cleanly separate
    into lines with all date to prepare to put in dictionary."""
    row = 0
    outputlist = []
    try:
        while row < len(inputlist):
            temp = ""
            while inputlist[row] != "":
                #search for next blank space, combine into temp vari and then write to list as 1 item
                temp += inputlist[row] + " "
                row += 1
                if row >= len(inputlist)-1:
                    break
            if temp != "":
                outputlist.append(temp)
            if temp == "":
                row += 1
    except IndexError:
        pass
    return outputlist

def field_checker(inputlist):
    """
    Takes input as a list where each item in the list is a passport entry,
    validates the passport entries are valid (correct fields present), and for 
    the valid entries will use regex to validate that the input is valid for each item.
    """
    first_pass_passports = []
    print(f"Total Passport Count: {len(parsed)}\n")

    # Reduce list to only check passports with all required fields
    for line in parsed:
        temp = 0
        for item in fields_required:
            if item in line:
                temp += 1
        if temp == 7:
            first_pass_passports.append(line)
    print(f"First Pass Passport Count: {len(first_pass_passports)}\n")

    # Regex time baby
    reg_byr = re.compile(r'.*byr:(?P<byr>\d{4})\b.*')
    reg_iyr = re.compile(r'.*(iyr:(?P<iyr>\d{4})\b).*')
    reg_eyr = re.compile(r'.*(eyr:(?P<eyr>\d{4})\b).*')
    reg_hgt = re.compile(r'.*(hgt:(?P<hgt>\d+)(?P<hgt_units>cm|in)\b).*')
    reg_hcl = re.compile(r'.*(hcl:#(?P<hcl>[0-9,a-f]{6})\b).*')
    reg_ecl = re.compile(r'.*(ecl:(?P<ecl>amb|blu|brn|gry|grn|hzl|oth)\b).*')
    reg_pid = re.compile(r'.*(pid:(?P<pid>\d{9})\b).*')

    approved = 0

    # check all items
    for line in first_pass_passports:
        
        match_byr = reg_byr.match(line)
        match_iyr = reg_iyr.match(line)
        match_eyr = reg_eyr.match(line)
        match_hgt = reg_hgt.match(line)
        match_hcl = reg_hcl.match(line)
        match_ecl = reg_ecl.match(line)
        match_pid = reg_pid.match(line)

        try:
            byr = int(match_byr.group('byr'))
            iyr = int(match_iyr.group('iyr'))
            eyr = int(match_eyr.group('eyr'))
            hgt = int(match_hgt.group('hgt'))
            hgt_units = match_hgt.group('hgt_units')
            hcl = match_hcl.group('hcl')
            ecl = match_ecl.group('ecl')
            pid = match_pid.group('pid')
            if (hgt_units == 'cm') and (hgt >= 150) and (hgt <= 193):
                hgt_bool = True
            elif (hgt_units == 'in') and (hgt >= 59) and (hgt <= 76):
                hgt_bool = True
            else:
                hgt_bool = False
            if  (byr >= 1920) and (byr <= 2002) and \
                (iyr >= 2010) and (iyr <= 2020) and \
                (eyr >= 2020) and (eyr <= 2030) and \
                (hgt_bool) and \
                (hcl != "") and (ecl != "") and (pid != ""):
                approved += 1
        except:
            continue

        print(match_byr.group('byr'))
        

    return approved
    

fields_expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

inputtext = load("Day4A-input.txt")
parsed = list_combine(inputtext)

approved = field_checker(parsed)


print(f'Valid Passport Count: {approved}\n')