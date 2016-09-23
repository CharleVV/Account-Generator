# _*_ coding:UTF-8 _*_
for line in open('F:\工作\无线校园网教师开户\教师账号生成\old.txt'):
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
    Account = 'js' + Phone
    Department = "".join(department)
    if IDCard is None:
        Generator_UserName = Name + '\t' + Account + "\t" + Phone + '\t' + Department
    else:
        Generator_UserName = Name + '\t' + Account + '\t' + IDCard + '\t' + Phone + '\t' + Department
    Username = open("F:\工作\无线校园网教师开户\教师账号生成\\New.txt", 'a')
    Username.writelines(Generator_UserName)
    Username.close()
