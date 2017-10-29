from mipcl_py.mipshell.mipshell import *

def t(e):
    return e[0]
def h(e):
    return e[1]
def u(e):
    return e[2]
def f(e):
    return e[3]
def c(e):
    return e[4]

class Fcnf(Problem):
    """The class for solving fixed charge network flow problems.
    """
    def model(self,G):
        """Build a model for the fixed charge network flow problem.

        Args:
           G (:obj:`dictionary`): flow network.

           G['Demands'] (:obj:`list` of :obj:`int`): list of demands at nodes.
           G['Arcs'] (:obj:`list` of :obj:`tuple`): list of edges:
              G['Arcs'][j] (:obj:`tuple` of :obj:`int`): tuple of five integers.
                 G['Arcs'][j][0] (int): tail of edge j.
                 G['Arcs'][j][1] (int): head of edge j.
                 G['Arcs'][j][2] (int): capacity of edge j.
                 G['Arcs'][j][3] (int): cost of edge j.
                 G['Arcs'][j][4] (int): fixed cost of edge j.

        Returnes:
           None.
        """
        self.G = G
        d, E = G['Demands'], G['Arcs']
        m, n = len(E), len(d)

        self.x = x = VarVector([m],"x")
        y = VarVector([m],"y",BIN)

        minimize(sum_(f(e)*y[j] + c(e)*x[j] for j,e in enumerate(E)))

        for v in range(n):
            sum_(x[j] for j,e in enumerate(E) if  h(e)==v)\
          - sum_(x[j] for j,e in enumerate(E) if  t(e)==v) == d[v]
		
        for j,e in enumerate(E):
            x[j] <= u(e)*y[j]

    def printSolution(self):
        """Prints the solution.
        """
        if self.is_solution is not None:
            if self.is_solution == True:
                d, E = self.G['Demands'], self.G['Arcs']
                x = self.x
                print('Flow cost = {:d}'.format(int(self.getObjVal() + 0.5)))
                for j,e in enumerate(E):
                    if x[j].val > 0.5:
                        print('flow({:d},{:d}) = {:d}'.format(t(e),h(e),int(x[j].val + 0.5)))
            else:
                print('Problem has no solution!')
        else:
            print('Please run optimize first')

if __name__ == '__main__':
    G = {
     'Demands': [-1,-2,-3,-4, -5,0,0,0,0, 0,0,0,0,0, 0,5,4,3,2,1],
       'Arcs': [
           (0, 1, 3, 1, 0), (1, 0, 3, 1, 0), (1, 2, 3, 1, 0),
           (2, 1, 3, 1, 0), (2, 3, 3, 1, 0), (3, 2, 3, 1, 0),
           (3, 4, 3, 1, 0), (4, 3, 3, 1, 0), (5, 6, 3, 1, 0),
           (6, 5, 3, 1, 0), (6, 7, 3, 1, 0), (7, 6, 3, 1, 0),
           (7, 8, 3, 1, 0), (8, 7, 3, 1, 0), (8, 9, 3, 1, 0),
           (9, 8, 3, 1, 0), (10, 11, 3, 1, 0), (11, 10, 3, 1, 0),
           (11, 12, 3, 1, 0), (12, 11, 3, 1, 0), (12, 13, 3, 1, 0),
           (13, 12, 3, 1, 0), (13, 14, 3, 1, 0), (14, 13, 3, 1, 0),
           (15, 16, 3, 1, 0), (16, 15, 3, 1, 0), (16, 17, 3, 1, 0),
           (17, 16, 3, 1, 0), (17, 18, 3, 1, 0), (18, 17, 3, 1, 0),
           (18, 19, 3, 1, 0), (19, 18, 3, 1, 0), (0, 5, 4, 2, 0),
           (5, 0, 4, 2, 0), (1, 6, 4, 2, 0), (6, 1, 4, 2, 0),
           (2, 7, 4, 2, 0), (7, 2, 4, 2, 0), (3, 8, 4, 2, 0),
           (8, 3, 4, 2, 0), (4, 9, 4, 2, 0), (9, 4, 4, 2, 0),
           (5, 10, 4, 2, 0), (10, 5, 4, 2, 0), (6, 11, 4, 2, 0),
           (11, 6, 4, 2, 0), (7, 12, 4, 2, 0), (12, 7, 4, 2, 0),
           (8, 13, 4, 2, 0), (13, 8, 4, 2, 0), (9, 14, 4, 2, 0),
           (14, 9, 4, 2, 0), (10, 15, 4, 2, 0), (15, 10, 4, 2, 0),
           (11, 16, 4, 2, 0), (16, 11, 4, 2, 0), (12, 17, 4, 2, 0),
           (17, 12, 4, 2, 0), (13, 18, 4, 2, 0), (18, 13, 4, 2, 0),
           (14, 19, 4, 2, 0), (19, 14, 4, 2, 0)
       ]
       }
    prob = Fcnf("gridNet")
    prob.model(G)
    # prob.optimize(False)
    prob.optimize(True)
    print("=========={}==========".format("(Exp. Soluition: 34)"))
    prob.printSolution()
