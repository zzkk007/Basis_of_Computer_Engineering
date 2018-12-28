
def create_dict():

    # 1 创建空字典
    dict1 = {}
    print(dict1)

    # 2 直接赋值创建
    dict2 = {'spam':1, 'egg':2, 'bar':3}
    print(dict2)

    # 3 通过关键词 dict 和关键参数创建
    dict3 = dict(spam = 1, egg = 2, bar = 3)
    print(dict3)

    # 4 通过二元元组列表创建
    list = [('spam', 1), ('egg', 2), ('bar', 3)]
    dict4 = dict(list)
    # dict4 = dict([('spam',1),('egg',2),('bar',3)])
    print(dict4)

    # 5 dict和zip结合创建

    dict5 = dict(zip('abc',[1,2,3]))
    print(dict5)

    # 6 通过字典推导式创建

    dict6 = {i:2*i for i in range(3)}
    print(dict6)

    # 7 通过 dict.fromkeys() 创建

    dict7 = dict.fromkeys(range(3),'x')
    print(dict7)

    # 8 其他

    list = ['x',1,'y',2,'z',3]
    dict8 = dict(zip(list[::2], list[1::2]),)
    print(dict8)





def Lesson7_1():

    q_horses_time = dict(q1 = 1.0, q2 = 2.0, q3 = 3.0)
    t_horses_time = dict(t1 = 1.5, t2 = 2.5, t3 = 3.5)

    q_horses = ['q1','q2','q3']
    t_horses = ['t1','t2','t3']


if __name__ == "__main__":

    #create_dict()
    Lesson7_1()



