g = {'Frankfurt': {'Mannheim':85, 'Wurzburg':217, 'Kassel':173}, 'Mannheim': {'Frankfurt':85, 'Karlsruhe':80},
     'Karlsruhe': {'Augsburg':250, 'Mannheim':80}, 'Augsburg': {'Karlsruhe':250, 'Munchen':84},
     'Wurzburg': {'Erfurt':186, 'Numberg':103,'Frankfurt':217}, 'Erfurt': {'Wurzburg':186},
     'Numberg': {'Wurzburg':103, 'Stuttgart':183,'Munchen':167}, 'Munchen': {'Numberg':167, 'Augsburg':84,'Kassel':502},
     'Kassel': {'Frankfurt':173, 'Munchen':502}, 'Stuttgart': {'Numberg':183}}

def BFS_weighted(graph, start, goal):

    distance = 0
    BFS = []
    queue = [start]
    lvl = {}
    sol = [goal]
    # SP = []
    while queue:
        node = queue.pop(0)
        if node not in BFS:
            BFS.append(node)
            if BFS[-1] == goal:
                for xtimes in range(len(sol)-1):
                    distance += graph[sol[xtimes]][sol[xtimes+1]]
                return BFS, sol, distance
            li = []
            # queue.extend(n for n in graph[node] if n not in path)
            for xNodes in graph[node]:
                if xNodes not in BFS:
                    queue.append(xNodes)
                    li.append(xNodes)

            if node not in lvl.keys():
                lvl[node] = li
                for n in li:
                    if n == goal:
                        yy = lvl.copy()
                        while sol[0] != start:
                            for k, v in yy.items():
                                if sol[0] in v:
                                    sol.insert(0,k)


                        # if len(SP) == 0:
                        #     for n in sol:
                        #         SP.append(n)
                        #     break
                        # print(SP)


                # get key ele value bt3to
        #     print("Q", queue)
        #     print("visited", path)
        # print("visited", path)
    # print("visited", path)
        # print("gra", graph)
        # print("lvls: ", lvl)
    return False

bfs, p , d = BFS_weighted(g, "Frankfurt", "Augsburg")
print("the BFS path is", bfs)
print("the direction is", p)
print("distance =", d, "KM")
# print(BFS_weighted(g, "Frankfurt", "Augsburg"))
print(BFS_weighted(g, "Frankfurt", 'Munchen'))


