# Investigating voter choice over time - Preliminary Report
### Leon Lam

I hope to investigate a population's change in attitude toward some 1-dimensional issue over time, given the possibility of interaction within the population. To that end, I hope to use a 2-dimensional cellular automaton based on Schelling's model of segregation and the Voter model.

#### Bibliography:

**SCHELLING, T. C. (1971).** *Dynamic models of segregation.* Journal of Mathematical Sociology 1: 143-186. [doi:10.1080/0022250X.1971.9989794]

The Schelling model is the foundation upon which the project will be built. Agents with fixed preferences relocate themselves in space if their neighbors are too different, causing segregation to develop over time.


**Hatna, Erez and Benenson, Itzhak (2012)** *'The Schelling Model of Ethnic Residential Dynamics:  Beyond the Integrated - Segregated Dichotomy of Patterns'* Journal of Artificial Societies and Social Simulation 15 (1) 6 <http://jasss.soc.surrey.ac.uk/15/1/6.html>. doi: 10.18564/jasss.1873

The paper uses a version of the Schelling Model where different groups have different thresholds for feeling unsatisfied, generating different types of segregation.


**Inés Caridi, Francisco Nemiña, Juan P. Pinasco, Pablo Schiaffino** *Schelling-voter model: An application to language competition* Chaos, Solitons & Fractals, Volume 56, November 2013, Pages 216-221, ISSN 0960-0779, http://dx.doi.org/10.1016/j.chaos.2013.08.013.
(http://www.sciencedirect.com/science/article/pii/S0960077913001720)

		
This paper uses a combination of the Schelling Model (where agents with fixed preferences relocate themselves) and a voting model (where agents change their preferences) to investigate segregation.


#### Experiments:


I've replicated a Schelling/voter model with a continuous range of values instead of two or more discrete values (where the population's opinion on a matter is not a binary 0/1, but a spectrum instead). 
Currently, each agent attempts to approach some sort of idealogical compromise with its neighbors unless its neighbors are too different in opinion (we define a certain threshold T - if the difference in two agents' opinions exceeds T, they are political enemies). 
In that case, an agent might choose to 'double down' on its opinion just like in real life. I suspect that the 'doubling down' may cause interesting behavior such as a small number of highly-opinionated agents separating two large but rather moderate populations.

I've run some preliminary tests on a 75 by 75 grid over 200 time steps with varying T thresholds. In a simulation of a more tolerant population (T is high), the population reaches homogenous compromise after some time.
As we decrease T, segregation patterns begin to emerge. Agents of differing opinions seem to become more 'finely' spaced as T decreases. 


#### Next Steps:


I intend to investigate this segregation phenomenon further, and introduce random interaction order instead of left-right top-down which might cause some sort of inherent bias.
I'd also like to be able to get some quantitative data out from the model: graphs of unpleasant interaction or segregation over time.
Another thing I'd like to do is start the model non-randomly with different patterns.

Other possible next steps are setting each agent's threshold independently (although this will require some finagling with numpy, since numpy seems to only store one numerical value per cell)
If there's time, I'd also like to extend the model to a social network modelled as a graph, so each agent may have a different number of neighbors (some may have less than 8, others might have more). We should see agents who have multiple lonely neighbors affecting the system much more than agents in a highly-connected cluster.


#### Learning goals:


My learning goals are to build something cool by adding bits of complexity to a simple system. Hopefully I'll get better at Python and gain additional understanding in this area of complexity science!
