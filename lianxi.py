import import_test

# name = 'HELLO World '
# name1 = '123'
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.lower())
# all = f'{name} {name1}'
# print(all)
#
# first_name = 'Hello'
# last_name = 'Python'
# full_name = f'{first_name}{last_name}'
# print(full_name)
#
# a = ' hello '
# b = a.strip()
# print(b)
# print(b)
# print(b)
#
# a=1
# b=2
# print(b/a)
# c=1_00000_000_00
# print(c)
# a,b,c = 1,'hh',{1,2,3}
# print(a,b,c)

# import this

# a = [1,3,5]
# print(a)
# a.remove(3)
# print(a)
# a.remove(2)
# del a
# print(a)

# a = [1,4,3,2,5]
# print(len(a))
#排序
# a = [1,4,3,2,5]
# sorted(a,reverse=True)
# print(a)
# print(sorted(a,reverse=True))
# a = ['a','c','b','e','d']

#for循环
# for i in range(3,31,3):
#     print(i,end=" ")

# for i in range(1,11):
#     print(i**3,end=" ")
# print('\n')
# aaa = list(i**3 for i in range(1,11))
# print(aaa)

#切片
# a = ["a","b","c","d"]
# b = a
# a.append("e")
# b.append("f")
#
# print(a)
# print(b)
# a = ["a","b","c","d"]
# print(a[0:3])
# a = ["a","b","c","d"]
# print(a[:3])
# a = ["a","b","c","d"]
# print(a[:2])
# a = ["a","b","c","d"]
# b = a[:]
# print(a)
# print(b)

# range步长
# number = list(range(1,6,2))
# print(number)

# 列表解析----求1-10的平方数
# square = [ value ** 2 for value in range (1,11)]
# print(square)

#元组
# a = (3,)
# print(a)
# print(type(a))

#if判断
# a = 1
# print(a == 1)
# a = 1
# print(a != 1)
#
# a = 1
# b = 2
# print(a == 1 and b == 2)
# print(a == b)

# list = ['a','b','c']
# # aa = 'a' in list
# # print('a' in list)
# # print(aa)
# if 'z' not in list:
#     print("'z'不在列表中")

# list = ['a','b','c']
# list = []
# if list:
#     print('列表有数据')
# else:
#     print('列表没有数据')
# car = 'sss'
# print("Is car == 'sss' ? I")
# print(car == 'sss')
# print("\nIs car == 'ccc'?IIII")
# print(car == 'ccc')

# a = 3
# if a < 1:
#     b = 1
# elif a < 2:
#     b = 2
# elif a < 3:
#     b = 3
# else:
#     b = 4
# print(b)

#字典
# a = {'color':'green','num':5}
# a["first"] = 1
# a["second"] = 2
# a['2021']='0721'
# print(a['color'])
# print(a)
# print(a,type(a))
# b = {'color':'green','num':5}
# for key,value in b.items():
#     print(key)
#     print(value)
# print(b)

##使用while循环处理列表和字典
# unlist = ['a','b','c']
# nlist = []
#
# while unlist:
#     currest = unlist.pop()
#     print(currest + '已经移除未认证列表')
#     nlist.append(currest)
#     print(currest + '已经添加到验证列表')
#
# print('已验证的列表为：')
# for nn in nlist:
#     print(nn.title())

##函数
# def test(name,age,xb):
#     print(f'Hello {name.title()},{xb}')
# test('wushuai',18,'男')

# def test(name,age = 18,xb = '男'):
#     print(f'Hello {name.title()},{age}，{xb}')
# test('wushuai',xb = 20)

##返回值
# def name(firstname,lastname):
#     fullname = f'{firstname}{lastname}'
#     return fullname
# My = name('Wu','shuai')
# print(My)

# def name(firstname,lastname,zjname = ''):
#     fullname = f'{firstname}{zjname}{lastname}'
#     return fullname
# My = name('Wu','shuai','ha')
# print(My)

# def name(firstname,lastname,age = None):
#     fullname = {'first':firstname,'last':lastname}
#     if age:
#         fullname['age'] = age
#     return fullname
# My = name('Wu','shuai',18)
# print(My)

##函数结合while循环
# def name(firstname,lastname):
#     fullname = f'{firstname}{lastname}'
#     return fullname
# while True:
#     print("请输入姓名：")
#     f_name = input('请输入姓：')
#     l_name = input('请输入名：')
#     My = name(f_name,l_name)
#     print(My)

# def name(firstname,lastname):
#     fullname = f'{firstname}{lastname}'
#     return fullname
# while True:
#     print("请输入姓名：")
#     f_name = input('请输入姓：')
#     if f_name == 'q':
#         break
#     l_name = input('请输入名：')
#     if l_name == 'q':
#         break
#     My = name(f_name,l_name)
#     print(My)

##函数修改列表
# def pri(unpris,comps):
#     while unpris:
#         curr = unpris.pop()
#         comps.append(curr)
#
# def show(comps):
#     for comp in comps:
#         print(comp)
#
# unpris = [1,2,3]
# comps = []
#
# pri(unpris[:],comps)
# show(comps)
# print(unpris)
# print(comps)

##传递任意数量的实参
# def test(abc,*ttt):
#     print(abc,ttt)
#     return ttt
#
# a = test(ttt)
# test(1,2,3)

# def test(*ttt):
#     print(ttt)
#     return ttt
# a = test(1,2,3)
# print(type(a))
#
# def test(**ttt):
#     print(ttt)
#     return ttt
# a = test(aa='a',bb='b',cc='c')
# print(type(a))

# def test(a,**ttt):
#     ttt['a'] = a
#     return ttt
# aa = test('hello',aa='a',bb='b',cc='c')
# print(aa)
# print(type(aa))

def test(abc,bbb = 1):
    print(abc,bbb)

test('ttt')

##调用别的py文件中的函数(模块导入)
# import_test.test('Wushuai')
# import_test.test('Wushuai1')