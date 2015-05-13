1.
Every code needs to change the filepath.

2.
I use an library called Lea (Discrete probability distributions in Python) to generate samples with one specific distribution
So, in my code, i import the "lea" library.
Find in there: https://code.google.com/p/lea/

Project 1: Inference
In Python, implement a data structure that represents the Bayesian Network in Figure 14.12a. This structure will need to represent the nodes, edges, and the CPTs for each node. Create a field for each node that specifies whether it is a query variable, an evidence variable, or neither. We will now use this structure to do inference.
1. Write a function that reads in a file called “inference.txt” file containing the following:
t,-,f,q
10
The order of elements on the 1st line corresponds to the order of nodes: Cloudy, Sprinkler, Rain, Wet Grass.
‘t’ means this variable is evidence and has been observed as true
‘f’ means this variable is evidence and has been observed as false
‘q’ means this variable is a query variable, we want to know the probability of this variable being true given the evidence: i.e. P(q | E)
‘-’ means this variable is neither the query nor evidence
The number in the 2nd line is the number of samples your algorithm will take
Read in the .txt file and set the relevant fields in your data structure.
2. Implement Rejection Sampling for this Bayesian Network. Create a file called “rejection.py” that reads in a .txt in the form above and uses the Rejection Sampling algorithm to compute P(q | E). Print the value out once you have computed it.
3. Implement Likelihood Weighting for this Bayesian Network. Create a file called “weighting.py” that reads in a .txt in the form above and uses the Likelihood Weighting algorithm to compute P(q | E). Print the value out once you have computed it.

Project 2: Filtering
In Python, implement a data structure that represents the DBN in Figure 15.13(a). This structure will need to represent the nodes, edges, and the CPTs for each node. We will now use this structure with a particle filter to compute the probability of rain given a series of umbrella observations.
1.  Write a function that reads in a file called “umbrellas.txt” containing the following type of input:
t,f,t,t,t
100
The elements on the 1st line correspond to a series of observations of umbrella in order of time.
‘t’ means the umbrella was observed as true at the given time step
‘f’ means the umbrella was observed as false at the given time step
The number on the 2nd line is the number of particles your particle filter will use
The number of time steps (and thus the number of observations) is not fixed, but there will be at least one time step.
2. Create a file called “particlefilter.py” that reads in umbrellas.txt in the form above and uses a particle filter to compute the probability of rain at the last time step given the series of umbrella observations in umbrellas.txt. Use the number of particles specified on the 2nd line of umbrellas.txt.
Writeup:
1. Run your particle filter on the following three cases:
1) t,f,t,f,t,f,t,f  
2) t,t,t,t,f,f,f,f
3) t,t,t,t,t,f
For each case, run your algorithm 30 times and graph the estimates your algorithm generates as you increase the number of particles (try increasing numbers of particles until the value converges). Average the results of the 30 runs for each number of particles and plot them in one graph per case. Include the graphs in your pdf.
2. For which of the three cases does the particle filter perform best (i.e. consistently produces a good estimate with few particles)? Explain why.
3. Why is producing a good estimate for the third case particularly unlikely with a small number of particles? Suggest a way to improve the particle filter to ameliorate this problem.
