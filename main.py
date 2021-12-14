
INF=0x3f3f3f3f
class graphic:
    def __init__(self,n,e):
        self.NoEdge=INF   #无边标记
        self.n=n          #顶点数
        self.e=e          #边数
        self.a=[]          #邻接矩阵
        self.vertices=[0,0,0,0]    #顶点数组
        for i in range(n):
            self.a.append([])
        for i in range(n):
            for j in range(n):
                self.a[i].append(self.NoEdge)

    #返回赋权有向图边数
    def GraphEdges(self):
        return self.e
    #返回赋权有向图G的顶点数
    def GraphVertices(self):
        return self.n

    #判断当前赋权有向图G中的边(i,j)是否存在
    def GraphExits(self,i,j):
        if(i<1 or j<1 or i>self.n or j>self.n or self.a[i][j] == self.NoEdge):
            return 0
        return 1
    #在赋权有向图G中加入边权为w的为(i,j);
    def GraphAdd(self,i,j,w):
        if(i<0 or j<0 or i>self.n or j>self.n):
            return
        self.a[i][j]=w

def createAWDGraph():
    n = eval(input("请输入图的顶点数目："))
    e = eval(input("请输入弧的数目："))
    graphic1 = graphic(n,e)
    vertices = input("请输入顶点信息(直接连续输入，不要使用空格或回车间隔，除非空格或回车是顶点存储的元素)：")
    for i in range(len(vertices)):
        graphic1.vertices[i]=vertices[i]
    print("构建邻接矩阵，请输入一条弧的起点、终点与权值,例如\"a,b,10\"")
    while(True):
        str=input("输入边:")
        if(str=="end"):
            break
        k = str.split(",")
        l=[0,0]
        #查找输入顶点的索引位置
        for i in range(len(graphic1.vertices)):
            if(k[0]==graphic1.vertices[i]):
                l[0]=i
            if(k[1]==graphic1.vertices[i]):
                l[1]=i
        #加边
        graphic1.GraphAdd(l[0],l[1],k[2])
    print("输出图的顶点: ",graphic1.vertices,sep='\t')
    print("输出图的邻接矩阵:\n",end='')
    for i in graphic1.vertices:
        print("{0:{1}^9}\t".format(i,""),end='')
    print("\n",end='')
    for i in range(graphic1.n):
        print(graphic1.vertices[i],end='\t')
        for j in range(graphic1.n):
            print("{0:{1}^10}\t".format(graphic1.a[i][j],""),end='')
        print("\n",end='')


#-------------------------------------------
#-------------------------------------------
#-------------------------------------------

class Inode:
    def __init__(self,v=None,weight=None,next=None):
        self.v=v
        self.weight=weight
        self.next=next
class Lgraphic:
    def __init__(self,n,e):
        self.n=n    #顶点数
        self.e=e    #边数
        self.a=[]   #邻接表数组
        self.NoEdge=0
        self.vertices=[0,0,0,0]
        for i in range(self.n):
            self.a.append(Inode(i))


    def GraphEdges(self):
        return self.e
    def GraphVertices(self):
        return self.n

    '''
    判断边是否存在，只需到a[i]中去查找是否有j结点即可
    v1 - 连接结点1 - 连接结点2
    v2 - 连接结点1 - 连接结点2
    v3 - 连接结点1 - 连接结点2
    v4 - 连接结点1 - 连接结点2

    '''
    def GraphExist(self,i,j):
        if(i<0 or j<0 or i>self.n or j>self.n):
            return 0
        p = self.a[i]
        while(p.next != None):
            p=p.next
            if(p.v==j):
                return True
        return False

    def GraphAdd(self,i,j,w):
        #判断(i,j)是否已经存在边
        if(i<0 or j<0 or i>self.n or j> self.n or self.GraphExist(i,j)):
            print("顶点输入错误")
            return
        k=self.a[i]
        p=self.a[i].next
        k.next=Inode(j,w,p)


def createLGraph():
    n=eval(input("请输入图的顶点数目:"))
    e=eval(input("请输入弧的数目:"))
    lgraphic = Lgraphic(n,e)
    vertices=input("请输入顶点信息(直接连续输入，不要使用空格或回车间隔，除非空格或回车是顶点存储的元素):")
    for i in range(lgraphic.n):
        lgraphic.vertices[i] = vertices[i]
    print("构建邻接矩阵，请输入一条弧的起点、终点与权值,例如\"a,b,10\"")
    while (True):
        str = input("输入边:")
        if (str == "end"):
            break
        k = str.split(",")
        l = [0, 0]
        # 查找输入顶点的索引位置
        for i in range(len(lgraphic.vertices)):
            if (k[0] == lgraphic.vertices[i]):
                l[0] = i
            if (k[1] == lgraphic.vertices[i]):
                l[1] = i
        # 加边
        lgraphic.GraphAdd(l[0], l[1], k[2])
    print("输出图的邻接表:")
    for i in range(lgraphic.n):
        p = lgraphic.a[i]
        print("{0}{1}{2}".format("[",lgraphic.vertices[p.v],"|->]"),end='\t')
        while(p.next != None):
            p=p.next
            print("(",p.v,"|",p.weight,")",sep='',end='\t')
        print("\n",end='')
if __name__ == '__main__':
    shit = graphic(4,0)
    #createAWDGraph()
    shit2 = Lgraphic(4,0)
    createLGraph()