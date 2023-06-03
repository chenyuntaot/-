import numpy as np
import queue


'''找出数据中最小的元素'''
def get2smallest(data):
    first = second = 1
    fid = sid =0 
    for idx, element in enumerate(data):
        if(element < first):
            second = first
            sid = fid 
            first = element
            fid = idx
        elif(element<second and element != first):
            second = element
    
    return fid, first, sid, second

'''定义哈夫曼节点'''
class Node:
    def __init__(self):
        self.prob = None
        self.code = None
        self.data = None
        self.left = None
        self.right = None    #元素值存储在叶节点
    
    def __lt__(self,other):
        if (self.prob < other.prob):  #定义优先树中排序规则
            return 1
        else:
            return 0
    
    def __ge__(self,other):
        if (self.prob > other.prob):
            return 1
        else:
            return 0

'''构建哈夫曼树'''
def tree(probabilities):
    prq = queue.PriorityQueue()    #优先级队列的构造函数
    for color,probability in enumerate(probabilities):
        leaf = Node()
        leaf.data = color
        leaf.prob = probability
        prq.put(leaf)
    while (prq.qsize() > 1):
        newnode = Node()   #创建新节点
        l = prq.get()
        r = prq.get()        #取出最小的两个节点
        #移除最小的两个节点
        newnode.left = l     #左侧节点较小
        newnode.right = r
        newprob = l.prob + r.prob   #新节点的概率，为左右概率之和
        newnode.prob = newprob
        prq.put(newnode)    #插入新节点，代替原有节点
    return prq.get()     #返回根节点，完成树的创建

'''对哈夫曼树遍历，得到编码'''
def huffman_traversal(root_node, tmp_array, f):
    if(root_node.left is not None):
        tmp_array[huffman_traversal.count] = 1
        huffman_traversal.count += 1
        huffman_traversal(root_node.left , tmp_array ,f)
        huffman_traversal.count -= 1
    
    if(root_node.right is not None):
        tmp_array[huffman_traversal.count] = 0
        huffman_traversal.count += 1
        huffman_traversal(root_node.right , tmp_array ,f)
        huffman_traversal.count -= 1

    else:
        huffman_traversal.output_bits[root_node.data] = huffman_traversal.count  #得到每个元素的编码值
        bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_traversal.count])
        color = str(root_node.data)
        wr_str = color + ' ' + bitstream + '\n'
        f.write(wr_str)    #保存到文件中
    return

if __name__ == '__main__':
    '''定义需要编码的图像'''
    image = np.array([
    [3,1,2,4],
    [2,4,0,2],
    [2,2,3,3],
    [2,4,4,2]
    ])

    '''计算每种元素出现的概率'''
    hist = np.bincount(image.ravel(),minlength=5)
    probabilities = hist / np.sum(hist)

    root_node = tree(probabilities)
    tmp_array = np.ones([4],dtype= int)
    huffman_traversal.output_bits = np.empty(5,dtype=int)
    huffman_traversal.count = 0
    f = open(r'DIP\notebook\chapter8\huffmancodes.txt','w')
    huffman_traversal(root_node,tmp_array,f)    #遍历树结构，给出编码