#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ɯɯ
���ڣ�2020/11/20
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name == "ʯͷ":
        number=int(0)
        return number
    elif name == "ʷ����":
        number=int(1)
        return number
    elif name == "ֽ":
        number=int(2)
        return number
    elif name == "����":
        number=int(3)
        return number
    elif name == "����":
        number=int(4)
        return number


    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��




def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==int(0):
        name="ʯͷ"
        return name
    elif number==int(1):
        name="ʷ����"
        return name
    elif number==int(2):
        name="ֽ"
        return name
    elif number==int(3):
        name="����"
        return name
    elif number==int(4):
        name="����"
        return name


    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    number=name_to_number(player_choice)
    comp_number=random.randint(0,5)
    number_to_name(comp_number)
    if number== 4 and comp_number == 2:
        print("��Ӯ��")
    elif number== 2 and comp_number == 0:
        print("��Ӯ��")
    elif number== 0 and comp_number == 4:
        print("��Ӯ��")
    elif number== 0 and comp_number == 3:
        print("��Ӯ��")
    elif number== 3 and comp_number == 1:
        print("��Ӯ��")
    elif number== 1 and comp_number == 4:
        print("��Ӯ��")
    elif number== 4 and comp_number == 3:
        print("��Ӯ��")
    elif number== 3 and comp_number == 2:
        print("��Ӯ��")
    elif number== 2 and comp_number == 1:
        print("��Ӯ��")
    elif number== 1 and comp_number == 0:
        print("��Ӯ��")
    elif number == comp_number:
        print("���ͼ��������һ����")
    else : print("�����Ӯ��")






    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)