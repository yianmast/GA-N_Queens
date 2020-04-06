#--------------------------------------------------------------------------------
# Name:      Genetic Algorithm- N-Queens Puzzle
#
#Required libs: random, tkinter, matplotlib, and statistics
#
#           to install libraries:  python -m pip install SomePackage
#
#functions:     gen_rad_population(N) genrates a random population; random solutions
#
#               fitness(chrom)) evaluates how good the solution is and return the fitness
#
#               Sort(sub_li) sorts solutions depending on their fitness
#
#               mutate(c) mutates/changes a solution 'slightly', i.e. only 1 integer
#
#               cross(pi,p2) crosses the 'genes' of two parents and generates four offsprings. You can choose the crossin point
#
#               board(sol, gen) prints solution and generation
#
#               gui(board) returns a graphic representation of the sollution
#
#               plot(genz,bestChrom) returns a plot with the the fitness of the best chromosome of each genration vs. generations
#
#
#               Represantation of solution: index of number + 1 --> column, number --> row
#
#               example. [1,2,3,4]   xxxq
#                                    xxqx
#                                    xqxx
#                                    qxxx
#
#               
#
#Author:    Ioannis Mastoras
#
#Created:   31 March 2020
#
#-----------------------------------------------------------------------------------
import random
import tkinter as tk
import matplotlib.pyplot as plt
from statistics import mean

#Basic Structure of GA
#Step 1: Generate random chromosomes of the form [n1,n2,n2...]
#Step 2: Evaluate the fitness of each chromosome
#Step 3: Keep the best chromosomes (top 50% in this case)
#Step 4: Crossover chromosomes from step 3; kill parents after birth
#Step 5: Mutate children and make them the new population (since parents are dead)
#Step 6: Repeat 2-5 untill you reach bst fitness!

def gen_rand_population(N):
    
    rand_population = [] #list of random initial solutions

    count = 0

    while count < 2*(N**2): #initial population size will be 2*N**2
        rand_chromosome = [random.randrange(1,N+1) for i in range(N)] #list with random numbers representing the state of the board
        rand_population.append(rand_chromosome) #add chromosome/solution to the population
        count += 1

    return rand_population
    
def fitness(chrom):
    
    horcol = 0 #hor(izontal) col(issions)
            
    for c in range(1,N+1):
        hor_dead = chrom.count(c) #same numbers are in the same row, thus they collide

        if hor_dead > 1: #to exclude collision with itself
            horcol += (hor_dead -1)
   

    digcol = 0 #diagonal collisions

    for i in range(0,N):
        for j in range(0,N):

            if abs(chrom[i]-chrom[j]) == abs(i-j) and i!=j: #in an NxN board, a diagonal line has slope 1.
                 digcol += 1                                #If defference in rows equals difference in columns,
                                                            #then slope is 1 and the queens kill each other
                                                             
   
    total_col = horcol + digcol/2 #we should only consider ONE collision per pair, thus divide by 2
    maxCol = (N*(N-1))/2 #max collisions if everything collides with everything
    fitness = maxCol - total_col 
    return fitness         

def Sort(sub_li): 
  
     return(sorted(sub_li, key = lambda x: x[1]))     
  

def Cross(p1,p2):

    n = cp #n equals chosen cross point
    
    c1 = p2[0:n] + p1[n:] #offspring 1
    c2 = p1[0:n] + p2[n:] #offspring 2

    m = random.randint(N//2,N-2)  #second cross point is random
    
    c3 = p2[0:m] + p1[m:] #offspring 3
    c4 = p1[0:m] + p2[m:] #offspring 4
 
    return c1,c2,c3,c4


def mutate(c):

    mutated = [] #mutated solution

    i = random.randint(1,N) #a random number for index
    n = random.randint(1,N-2)


    c[n] = i #change a random number with a random number; in the queen problem that means move a random queen to a random place

    mutated = c

    return mutated
    



def board(sol,gen):

    
    board = []

    for x in range(N):                  #
        board.append(["X"] * N)         #
                                        # creates the board
    for r in sol:                       #
        x = sol.index(N-sol.index(r))   #
        board[sol.index(r)][x] = 'Q'    #

    print('\n \n')
    print('===========================================================')
    print("Generation ", gen,'\n')
    print('One solution is \n',sol)
    for b in board:
        print(b)
        
    gui(board) #gui of the solution

    #flip the board to get another solution
    
    gui(list(reversed(board))) #gui of 2nd solution

    sol.reverse() #rotate the board to get 2 more solutions

    board2 = []

    for x in range(N):
        board2.append(["X"] * N)

    for r in sol:
        x = sol.index(N-sol.index(r))
        board2[sol.index(r)][x] = 'Q'

    
    print('Another solution is \n',sol)
    for b in board2:
        print(b)
    gui(board2)

    board2.reverse()
    gui(board2)      


def gui(board):
    
    window = tk.Tk() #create a window
    window.title("Board")  

    for i in range(N):
        for j in range(N):    #create an NxN grid
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=2
            )
            frame.grid(row=i, column=j)
            if board[i][j] == 'X':
                label = tk.Label(master=frame, text=f"%s"%board[i][j],width=80//N,height=32//N,bg='blue')

            else:
                label = tk.Label(master=frame, text=f"%s"%board[i][j],width=80//N,height=32//N,bg='red')

            label.pack()

    window.attributes('-topmost', True)
    window.mainloop()

def plot(genz,bestChrom):

    plt.plot(genz, bestChrom,'bo-') #plt,plot(x,y,line format)
    plt.ylabel('Fitness of Best Chromosome From Each Generation')
    plt.xlabel('Generation')
    plt.title("Best Fitness vs. Generation")
    plt.grid(True)
    plt.axis([0, len(genz)+0.1, 0, 105]) #plt.axis(x_min,x_max,y_min,y_max)

    #to label the points
    for x,y in zip(genz,bestChrom): 

        label = "{:.2f}".format(y)

        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,15), # distance from text to points (x,y)
                     ha='center') # horizontal alignment 
    plt.show()



N = int(input(" Size of population (more than 3) ")) 

cp = int(input("cross point (between 0 and N: " ))
   
population = gen_rand_population(N) #initial population is randomly generated

bestFit = (N*(N-1))/2 #fitnes is max collisions - actual collisions. When there are no collision, you have best fitness
generation = 1

bestChrom = [] #stores best chromoseomes from each gen for the plot
genz = [] #stores track of generation for the plot

while True:

    genz.append(generation) #keeps track of the generation

    fit = [] #list with fitness of each cromosome
    for chrom in population:
        fit.append((fitness(chrom)/bestFit)*100) #convert fitness to percentage

    popfit = [] #chromosome and fitness list --> [[chrom1,fitness1]....]
    for j in range(0,len(population)):
        popfit.append([population[j],fit[j]])

    sortpopfit = Sort(popfit) #sort in terms of fitness
    
    Sum = 0 #sum of fitness of each generation
    toCross = [] #a list with the best chromosomes which we will cross
    
    print('=============Generation ',generation,'================== ')

    for k in range(len(popfit)//2,len(popfit)): #only top 50% of the population makes it
        print("Chromosome ==",sortpopfit[k][0], "  Fitness ==",round(sortpopfit[k][1],1),'%')

        toCross.append(sortpopfit[k][0])

        Sum += sortpopfit[k][1]

    avg = Sum/len(toCross) #average fitness of generation

    print("Average Fitness of Generation ", round(avg,1),'%')
    
    bestChrom.append(round(sortpopfit[-1][1],1))

    
    if sortpopfit[-1][1] == 100: #if a solution is generated
        board(sortpopfit[-1][0],generation) #call the board function to print it
        break #stop the loop

    else:  
        crossed = [] #stores new offsprings
        for t in range(0,len(toCross)-1,2):
            for c in Cross(toCross[t],toCross[t+1]): #crosses chromosomes from the to cross list; every chromosome s crosses with the crhomosomes next to it
                crossed.append(c)

        mutated = []  #stores mutated chromosomes
        for f in range(0,len(crossed)):
            mutated.append(mutate(crossed[f])) #mutate each of the offsprings

        population = mutated #new populations consists of the offsprings; 'kill' all parents after birth
        generation += 1

plot(genz,bestChrom)
