# _*_ coding:UTF-8 _*_
for line in open('Path\old.txt'):
    name_txt = list(line[0:3])
    if '\t' in name_txt:
        name = list(line[0:2])
        idcard = list(line[3:21])
        if "\t" in idcard:
            IDCard = None
            phone = list(line[3:14])
            department = list(line[15::])
        else:
            phone = list(line[22:33])
            department = list(line[34::])
            IDCard = "".join(idcard)
    else:
        name = list(line[0:3])
        idcard = list(line[4:22])
        if "\t" in idcard:
            IDCard = None
            phone = list(line[4:15])
            department = list(line[16::])
        else:
            phone = list(line[23:34])
            department = list(line[35::])
            IDCard = "".join(idcard)
    Name = "".join(name)
    Phone = "".join(phone)
    Department = "".join(department)
    if IDCard is None:
        Generator_UserName = Name + '\t' + 'js' + Phone + "\t" + Phone + '\t' + Department + '\n'
    else:
        Generator_UserName = Name + '\t' + 'js' + Phone + '\t' + IDCard + '\t' + Phone + '\t' + Department + '\n'
    Username = open("('Path\\New.txt", 'a')
    Username.writelines(Generator_UserName)
    Username.close()
