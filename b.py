
def gen_data(text):
    return text.lower().split()
def func_dict(word_list):
    """
    方法一：使用字典
    :param word_list:
    :return:
    """
    count_dict = {}
    for item in word_list:
        count_dict[item] = count_dict[item] + 1 if item in count_dict else 1
    return sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
f = open(r'provers.txt')
c=gen_data(f.read().replace(".",''))
f.close()
print(func_dict(c))
