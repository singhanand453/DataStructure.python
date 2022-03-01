def printparent(root,adj,parent):
    if(parent == 0):
        print(root)
    else:
        print(parent)
    
    for  i in adj[root]:
        if( i != parent):           
            printparent(i , adj , root)

def printchildren(root , adj):
    q=[]
    q.append(root)
    vis =[0]*len(adj)
    while(len(q) > 0):
        node = q[0]
        q.pop(0)
        vis[node] = 1
        print(node, "->" , end=" ")

        for i in adj[node]:
            if(vis[i] == 0):
                print(i," ",end=" ")
                q.append(i)
        print("\n")
            

N = 7
Root = 1
adj = []
for i in range(0, N+1):
    adj.append([])

adj[1].append(2)
adj[2].append(1)
 
adj[1].append(3)
adj[3].append(1)
 
adj[1].append(4)
adj[4].append(1)
 
adj[2].append(5)
adj[5].append(2)
 
adj[2].append(6)
adj[6].append(2)
 
adj[4].append(7)
adj[7].append(4)

printparent(Root, adj, 0)
printchildren(Root, adj)