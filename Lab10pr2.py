def isClique(G,X,k):
    '''
    checks whether the set of vertices X is a k-clique in the graph G (which
    is given as an adjacency list stored in a dictionary).

    Keyword Arguments:
    G -- Graph (stored as ajacency list dictionary)
    X -- Set of vertices
    k -- The amount of interconnected verticies you want to check (does that amount exist)

    '''
    interconnected = 0 #count how many interconnected verts have been found
    tempset = set([])
    originalAsLst = []
    connections = 0

    if len(X) != k:
        return False
    for i in X: 
        originalAsLst.append(i) #make keep the original list in this so sets can be modified

    while interconnected != k: #Stops if desired amount has been found
        for Q in originalAsLst:
            tempset = set(originalAsLst)
            tempset.remove(Q)
                        
            if len(X) == 0:
                break #breaks out to other break statement, we're done.
            
            for i in tempset:
                if i in G[Q] and Q in G[i]:
                    connections += 1
                    
            if connections == len(tempset): 
                X.remove(Q)
                interconnected += 1
                
            connections = 0
            
        break
    
    if interconnected ==  k:
        return True
    else:
        return False

'''The runtime of the program is O(n) to the power of k. It's not NP, mainly
because it's a k clique, which is different from just a clique in that a clique
has no particular limited size. A K-clique is limited by the k value. It's o(n)
to the power of k because it uses a nested structure to make simultaneous comparisons
(is i in G[Q] and is Q in G[i]).'''
        
'''G = {1:[2,4,5,7],2:[1,3,4,5,7],3:[2,6,7],4:[1,2,5,7],5:[1,2,4,7],6:[3,7],7:[1,2,3,4,5,6]}
X ={1,2,4,5,6,7}
print(isClique(G,X,1))'''
