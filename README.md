# SPRACE-LLP

This repository is being used for studies about Long Lived Particles (LLPs), and sharing codes regarding the simulation of these particles using [MadGraph](https://arxiv.org/abs/1405.0301), [Pythia](https://arxiv.org/abs/1410.3012) and [Delphes](https://arxiv.org/abs/1307.6346) (and CMSSW in the near future).

## Using Madgraph+Pythia+Delphes to simulate LLPs

To run the model described in the paper [LHC-friendly minimal freeze-in models](https://arxiv.org/abs/1811.05478) using Madgraph+Pythia+Delphes, the first step is to download the UFO files available at (FIMP - UFO)[http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC]. The second step is that there is a minor change that need to be made: the PID of one of the new particles is the same as the one from the neutral pion (111), and MadGraph don't perform the simulation in this case. This need to be changed in the files 'particles.py' and 'parameters.py' (the files with the changes are in the branch Delphes).
