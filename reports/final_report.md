# Investigating voter choice over time – Final Report
### Leon Lam


#### Background:

The topic of radicalization - religious, political or otherwise - is a relevant one in today's society. Why do certain topics result in consensus while others divide the population so drastically? In this vein, we investigate a population's change in attitude toward some 1-dimensional issue over time, given the possibility of interaction within the population. Our model of choice is a 2-dimensional cellular automaton based on Schelling's model of segregation (where agents on a grid have fixed qualities and move around if they're surrounded by too many agents different from them) and the Voter model (where agents in a graph have a probability to change their mind based on how many agents around them hold a different view).

#### Experiments:

##### Experiment 1


*Question:* 


How does the model behave when agent tolerance for other opinions changes?


*Methodology:*


We replicate a Schelling/voter model with a continuous range of values instead of two or more discrete values (where the population's opinion on a matter is not a binary 0/1, but a spectrum instead).

Currently, each agent attempts to approach some sort of ideological compromise with its neighbors unless its neighbors are too different in opinion (we define a certain tolerance threshold T - if the difference in two agents' opinions exceeds T, they are political enemies). 

In that case, an agent might choose to 'double down' on its opinion just like in real life. I suspect that the 'doubling down' may cause interesting behavior such as a small number of highly-opinionated agents separating two large but rather moderate populations.


*Result:*


We run some preliminary tests on a 75 by 75 grid over 200 time steps with varying T thresholds. In a simulation of a more tolerant population (T is high), the population reaches homogenous compromise after some time.

As we decrease T, segregation patterns begin to emerge. Agents of differing opinions seem to become more 'finely' spaced as T decreases.

![T=0.1](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/First%20Pass/T_0.1%2075x75.PNG)

*T=0.1.*

![T=0.3](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/First%20Pass/T_0.3%2075x75.PNG)

*T=0.3.*

![T=0.7](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/First%20Pass/T_0.7%2075x75.PNG)

*T=0.7.*

We then run an exhaustive sweep of T from 0.0 to 1.0. The results are as follows:

![Sweeping T from 0.0 to 1.0](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Second%20Pass/Critical%20point%20-%20t%20on%20x%20axis%20vs%20average%20opinion%20difference%20on%20y%20axis.PNG)

*Exhaustive sweep from T=0.0 to T=1.0.*

*Interpretation:*


Threshold T definitely has a large qualitative impact on the system behavior. A distinct change around T=0.4 to T=0.6 seems to indicate the presence of a critical point in that area, which prompts further investigation.


##### Experiment 2


*Question:* 


What value range of tolerance threshold T gives us the most noticeable change?


*Methodology:* 


The model has been optimized slightly and updated so each agent interacts with all of its neighbors in random order. Previously, it was left-right, top-down. The model can also measure segregation, which is calculated as the average difference between each cell and its neighbors.

*Result:* 


An exhaustive sweep of T (from T=0.0 to T=1.0) in Experiment 1 showed us that the region of greatest change is between T=0.4 and T=0.6. We then perform a closer sweep, which reveals T=0.43 to T=0.5 to be the critical region.

![Closer sweep from T=0.4 to 0.6](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Second%20Pass/Critical%20point%20-%20t%20on%20x%20axis%20vs%20average%20opinion%20difference%20on%20y%20axis%2040x40%20500%20steps%208%20iterations.PNG)

*Closer sweep from T=0.4 to 0.6.*


*Interpretation:*


Our system randomly generates starting values for its agents, so on average the difference between any two agents is likely to be around 0.5. This is probably why landscapes with T>0.5 result in low segregation after a few timesteps. Being able to see an individual opinion landscape change over time might offer more insight. 


##### Experiment 3


*Question:* 


What does an individual opinion landscape look like? How does its segregation vary over time? How does threshold T affect this?


*Methodology:*


We track the segregation of a landscape over time, and take slices of the landscape at time=0, at time=12 (trial and error, time=12 looks distinct enough from both beginning and end states) and at time=200 (roughly steady state). We then plot 3 slices of the landscape alongside its segregation over time, and investigate the behaviors of landscapes with different threshold T.


*Results:*


From T=0.44 to T=0.5, we see a change from high steady state segregation to extremely low steady state segregation. This agrees with the results of Experiment 2, but for some T values which have a high steady state segregation, an interesting dip in segregation happens in the first 25 timesteps before the system returns to a higher steady state segregation.

![T=0.4495](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Third%20Pass/4495.png)

*T=0.4495. The three slices are time=0, time=12, time=200, and the red line measures segregation (y-axis) vs time (x-axis).*

![T=0.45](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Third%20Pass/test45.png)

*T=0.45.*

![T=0.46](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Third%20Pass/test46.png)

*T=0.46.*


*Interpretation:*


We believe there is a critical point in the system around T=0.45 or so, which causes the large variation in steady state segregation. We’re not entirely sure why the dip is happening, but hypothesize that while most of the grid is homogenizing, some limited pockets of the grid are radicalizing. When most of the grid has reached steady state, the radicalizing influence exerted by the pockets of the grids with extreme values becomes more relevant, and increases the segregation of the grid.


##### Experiment 4


*Question:*


To what extent to other variables affect system behavior?


*Methodology:*


We fiddled around with different variables. In particular, we changed the number of timesteps, grid size, and how much each agent is affected by its neighbors. 


*Results:*

None of them had appreciable impact on the overall trend of the results, although a small grid size (20x20 and below) results in a lot more ‘swingy’ results, since the impact of random chance was larger.


![1](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Third%20Pass/sweep2_k_32.png)
![2](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Third%20Pass/sweep1_k_32.png)
![3](https://github.com/leonjunwei/ComplexityScience16Project/blob/master/code/Third%20Pass/sweep3_k_16_200steps.png)

*These graphs were created by different sweeps with different variable values. We named them poorly and can't tell them apart now.*

*Interpretation:*


This isn't too much of a surprise, since we’ve already found out that the systems all reached a rough steady state after 200 steps or so. Increasing the timesteps just shows us more of steady state, increasing grid size makes landscapes less random from trial to trial, and the strength of each agent’s interactions only affects the rate of convergence to steady state. 


#### Future Work:

Starting the model non-randomly with different patterns could be useful to investigate how the arrangements of cells affects the end state. For example, a small number of highly-opinionated agents creating a boundary between two groups of moderate agents might be enough to radicalize the entire landscape. 

Extending the model to a social network modelled as a graph would allow us to investigate the importance of key agents (who have more connections than the mean) in influencing a population's opinion. For example, a small number of highly-opinionated agents could radicalize an entire network if they had enough connections between them.


#### Bibliography:

**SCHELLING, T. C. (1971).** *Dynamic models of segregation.* Journal of Mathematical Sociology 1: 143-186. [doi:10.1080/0022250X.1971.9989794]

The Schelling model is the foundation upon which the project will be built. Agents with fixed preferences relocate themselves in space if their neighbors are too different, causing segregation to develop over time.


**Hatna, Erez and Benenson, Itzhak (2012)** *'The Schelling Model of Ethnic Residential Dynamics:  Beyond the Integrated - Segregated Dichotomy of Patterns'* Journal of Artificial Societies and Social Simulation 15 (1) 6 <http://jasss.soc.surrey.ac.uk/15/1/6.html>. doi: 10.18564/jasss.1873

The paper uses a version of the Schelling Model where different groups have different thresholds for feeling unsatisfied, generating different types of segregation.


**Inés Caridi, Francisco Nemiña, Juan P. Pinasco, Pablo Schiaffino** *Schelling-voter model: An application to language competition* Chaos, Solitons & Fractals, Volume 56, November 2013, Pages 216-221, ISSN 0960-0779, http://dx.doi.org/10.1016/j.chaos.2013.08.013.
(http://www.sciencedirect.com/science/article/pii/S0960077913001720)

		
This paper uses a combination of the Schelling Model (where agents with fixed preferences relocate themselves) and a voting model (where agents change their preferences) to investigate segregation.

