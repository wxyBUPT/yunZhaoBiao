#coding=utf-8
__author__ = 'xiyuanbupt'
def foo():
    def plot():
        '''
        画图模块，暂时只是做一个演示
        :return:
        '''
        xlbael=[1,2,3,4]
        ylbael=[2,3,4,5]
        import matplotlib
        import matplotlib.pylab
        fig=matplotlib.pylab.figure()
        ax=fig.add_subplot(111)
        ax.scatter(xlbael,ylbael)
        matplotlib.pylab.show()

    plot()

if __name__=="__main__":
    foo()
