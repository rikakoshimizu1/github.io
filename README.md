# Timon Lepidus (Ocellated Lizard) Scale Pattern Simulation

## Overview
This project uses cellular automata to simulate the dynamic skin scale patterns of the *Timon lepidus* (ocellated lizard). By varying key parameters, the simulation captures how the lizard's scale patterns evolve from juvenile to adult stages. Through local cell interactions, the model produces emergent global patterns that closely resemble those found in nature, offering a computational perspective on biological pattern formation. 

## Background
The formation of natural patterns such as those on seashells, snowflakes, or animal coats, has long fascinated both biologists and mathematicians. Cellular automata is a mathematical modeling technique that uses grids of discrete cells updated by local rules. This method provides a powerful framework for studying how complex patterns emerge. Building on the work of Manukyan et al. in *A Living Mesoscopic Cellular Automaton Made of Skin Scales* (2017) this project applies cellular automata to replicate the striking scale arrangements observed in *Timon lepidus*, a species known for its mosaic-like skin patterns. By simulating the rules that govern cell behavior and interaction, the model demonstrates how biologically realistic structures can form through simple, local interactions. This work builds on research in computational biology and contributes to the broader understanding of natural pattern formation. 

## Features
 - Callular automata simulation on a 2D hexagonal grid
 - Scale coloring (black/green) based on biological neighbor rules
 - Frequency tracking of neighbor relationships
 - Support for multi-iteration simulation
 - Visual graphs of scale state frequencies and transitions
 - Several manipulations including:
  - Random initialization
  - Ratio-based probability selection
  - Neighbor-based probabilistic color flipping

## Key Aspects
 - Custom transition rules modeled after the biological development of lizard scale patterns
 - Focus on local neighbor interactions to generate complex, emergent global patterns
 - Balance between biological accuracy and computational simplicity
 - Simulation and visualization implemented entirely in Python
 - Utilizes hexagonal grids to closely mirror natural lizard scale arrangement

## Challenges
 - Defining a rule set that produce biologically realistic patterns while remaining computationally simple.
 - Managing performance issues related to memory and processing time, especially on larger grids.
 - Ensuring consistent, stable pattern evolution without the patterns getting stuck or showing unwanted glitches. 
 - Comparing simulated results to biological data and photographs of *Timon lepidus* to assess accuracy and improve the model.

## Future Work
 - Analyze the impact of lizard gender on pattern transitions
 - Randomize update direction (vs. left-to-right sweeps)
 - Refine simulation to model the trough at 5 black neighbors
 - Improve CA logic to better reflect natural pigment diffusion

## Acknowledgements
This project was completed as part of a senior capstone in Mathematics, with valuable guidance from Dr. Rickert.
