# Account-Generator
一个账号生成器，将只含姓名和电话号码的文本文件转换为加特定前缀的账号。
文本格式为：
Name	IDCard	Phone	Department
Judy	11010220120901269X	13099992222	Network-Center	
其中每列以TAB作为分隔
生成的文本格式为：
Name	Account	IDCard	Phone	Department
Judy	js13099992222	11010220120901269X	13099992222	Network-Center
