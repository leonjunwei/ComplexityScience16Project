# Investigating voter choice over time
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


#### Experiments to replicate:


I'm interested in replicating a Schelling/voter model with a continuous range of values instead of two or more discrete values (for example, the population's opinion on a matter might not be a simple 0/1, but a spectrum instead). Each agent should attempt to approach some sort of idealogical compromise with its neighbors, unless some of its neighbors are too different in opinion: in that case, an agent might choose to 'double down' on its opinion just like in real life. I suspect that the 'doubling down' may cause interesting behavior such as a small number of highly-opinionated agents separating two large but rather moderate populations.


If there's time, I'd also like to extend the model to a social network modelled as a graph, so each agent may have a different number of neighbors (some may have less than 8, others might have more). We should see agents who have multiple lonely neighbors affecting the system much more than agents in a highly-connected cluster.


#### Learning goals:


My learning goals are to build something cool by adding bits of complexity to a simple system. Hopefully I'll get better at Python and gain additional understanding in this area of complexity science!
