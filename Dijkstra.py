
# TAHSIN SHAMSUL
# Dijkstra's Algorithm
# CS 242 - Strout


################ Initialize ############
ADJ = dict() # Adjacency list  Key:(Neighbor,Cost)
GRAPH = dict() # Graph list    Key:[visited, cost, previous]

Text = str(input('Enter graph file: '))
fin = open(Text)
Start = str(input('Enter starting point: '))
Dest = str(input('Enter destination point: '))
ShortPath = []
Finalized = []

########################################

def Readfile(File):
        for line in fin.readlines():
            X = line.split()
            if X != []:
                #print(X)
                if X[0] == 'a':
                    key = X[1] 
                    value = (X[2], int(X[3])) # (Neighbor, Cost)
                    if key not in ADJ:
                        Finalized.append(key)
                        ADJ[key] = []
                        if key == Start:
                            GRAPH[key] = [False, 0, None]
                        else:
                            GRAPH[key] = [False, float('inf'), None]    
                    ADJ[key].append(value)
                else:
                    pass
        return



def Queue():
    if Finalized == []:
        return
    
    Priority = [] # Creates a new priority list every time this function
                  # is called so it can add the updated values of each vertex
    
    for key in Finalized:
        if GRAPH[key][1] != float('inf'): 
            Data = (GRAPH[key][1], key)
            Priority.append(Data)
            
    Priority.sort() #Sorts the list based on cost, so 0th element is smallest value
    
    NextCurrent = Priority[0][1]
    #print('Priority: ', Priority, NextCurrent)
    
    #Algorithm(NextCurrent) #Recurse with next smallest non finalized value
    
    return NextCurrent

def Algorithm():

        if Finalized == []:
            return
        
        while Finalized != []:
            Current = Queue() #Queue() # Call this Fn to determine which vertex
                            # has the smallest cost in order to be the next Current
            #print('CURRENT: ',Current)
            
            CurrCost = GRAPH[Current][1]#Current cost of vertex
                                        #we are checking neighbors of

            for vertex in ADJ[Current]: # vertex = (neighbor, cost)

                if GRAPH[vertex[0]][0] != True: # if vertex is not finalized, update it
                    #GRAPH[vertex[0]] is [ visited, cost, prev]
                    
                    VertexCost = GRAPH[vertex[0]][1] #Current cost of nonfinalized vertex
                    #Conditions to update
                    if VertexCost == float('inf'):
                        # if infinity, then update the cost
                        GRAPH[vertex[0]] = [False, vertex[1] + CurrCost, Current]
                        
                    elif VertexCost > vertex[1] + CurrCost:
                        # if Old cost is larger than New cost, then update with New cost
                        GRAPH[vertex[0]] = [False, vertex[1] + CurrCost, Current]
            
            GRAPH[Current][0] = True
            Finalized.remove(Current)
            #print(Finalized)
            
        else:
            return




def ShortestPath(endpoint):
        if Start in ShortPath:
            Path = []
            for i in range(len(ShortPath)-1,-1,-1):
                #print(ShortPath[i])
                Path.append(ShortPath[i])
            #Dist = GRAPH[Dest][1]
            print('Minimum distance between', Start,'and', Dest,'is: ', GRAPH[Dest][1])
            print('Shortest Path: ', Path)
            return
        else:
            ShortPath.append(endpoint)
            Point = GRAPH[endpoint][2]
            #print(ShortPath, Point)
            ShortestPath(Point)


################### Implementation ######################
def MAIN():
    
    Readfile(Text)
    Algorithm()

##    for i in GRAPH.keys():
##        print(i,':',GRAPH[i])
        
    ShortestPath(Dest)

MAIN()
input('Press ENTER to close')
#########################################################
