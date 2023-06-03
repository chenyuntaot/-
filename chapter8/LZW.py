string = 'abbababac'

#将编译表初始化为包含所有可能单字字符，当前前缀P初始化为空
dictionary = {'a':1,'b':2,'c':3}  
last = 4
p = ''  #prefix
result = []
for c in string:    #当前字符C:=字符流中的下一个字符
    pc = p+c
    #判断p+c是否存在编译表中
    if pc in dictionary:     # 若存在，则用C扩展P,即P:=P+C
        p = pc

    else:          #若不存在，则输出当前前缀P对应的码字，并将P+C添加回编译表中，并令P:=C
        result.append(dictionary[p])
        dictionary[pc] = last
        last += 1
        p = c
#没有码字要译，则将代表当前前缀P的码字输出到码字流，结束
if p != '':
    result.append(dictionary[p])
print(result)
