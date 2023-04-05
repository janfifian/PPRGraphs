import tkinter as tk
import networkx as nx

# This method checks if in graph G the vertex i can be reduced to j.
def isIReducibleToJ(G : nx.Graph, v: int, vprim: int) -> bool:
    for w in G[v].keys():
        if (w != vprim) and (w not in G[vprim].keys()):
            return False
    return True

# This method verifies if G is a PPR graph or not.
def recognizePPRGraph(G : nx.Graph):
    Q = set()
    for v in G.nodes:
        Q.add(v)
    while Q.__len__()>0:
        v = Q.pop()
        currentNodes = list(G.nodes)
        for vprim in currentNodes:
            if vprim != v:
                if isIReducibleToJ(G, v, vprim):
                    for w in G[vprim].keys():
                        if w != v:
                            Q.add(w)
                    G.remove_node(v)
                    break

    if len(G.nodes) == 1:
        return True
    else:
        return False

mainGUIWindow = tk.Tk()

labelNumberOfVertices = tk.Label(text = "Graph size")
labelNumberOfVertices.pack()

entryNumberOfVertices = tk.Entry()
entryNumberOfVertices.pack()

labelProbability = tk.Label(text = "Edge probability")
labelProbability.pack()

entryProbability = tk.Entry()
entryProbability.pack()

labelNumberOfTrials = tk.Label(text = "Number of MC trials")
labelNumberOfTrials.pack()

entryNumberOfTrials = tk.Entry()
entryNumberOfTrials.pack()

launchButton = tk.Button(text="Start!")
launchButton.pack()

def performMonteCarloTesting(args):
    n = int(entryNumberOfVertices.get())
    T = int(entryNumberOfTrials.get())
    p = float(entryProbability.get())

    PPRcounter = 0.0

    for J in range(T):
        Q = nx.gnp_random_graph(n,p) # generates random graph on n vertices
                                     # where each edge is added with probability p
        if recognizePPRGraph(Q): PPRcounter+=1.0

    print(PPRcounter/T)

launchButton.bind("<Button-1>", performMonteCarloTesting)

mainGUIWindow.mainloop()