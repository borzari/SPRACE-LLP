# SPRACE-LLP

This repository is being used for studies about Long Lived Particles (LLPs), and sharing codes regarding the simulation of these particles using [MadGraph](https://arxiv.org/abs/1405.0301), [Pythia](https://arxiv.org/abs/1410.3012) and [Delphes](https://arxiv.org/abs/1307.6346) (and CMSSW in the near future).

## Using Madgraph+Pythia+Delphes to simulate LLPs

To run the model described in the paper [LHC-friendly minimal freeze-in models](https://arxiv.org/abs/1811.05478) using Madgraph+Pythia+Delphes, the first step is to download the UFO files available at [http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC](FIMP - UFO). The second step is to move the folder that contain the files to the models folder inside MadGraph. There is a minor change that need to be made in two of those files: the PID of one of the new particles (charged parent) is the same as the one from the neutral pion (111), and MadGraph don't perform the simulation in this case. This need to be changed in the files 'particles.py' and 'parameters.py' (the files with the changes are in the branch Delphes).

After that, you just need to run MadGraph using '/bin/mg5_amc', import the model 'import model Name_of_the_folder', generate the process of interest (such as 'generate p p > ~he ~HE, (~he > l- ~s0), (~HE > l+ ~s0)', but this depends on the type of the charged parent), use the 'output' command to create a folder in which the runs will be saved and 'launch' the simulation. Just remember to add the showering/hadronization and the detector simulation softwares.

There is a shortcut to all of what was described above that is by using a configuration file that has all the options that need to be active and that will input the necessary commands. Inside the folder 'configuration_files' in the Delphes branch are the files needed to perform this. The 'param_card.dat', 'run_card.dat' and 'delphes_card.dat' are also necessary. Any change in the model or the run parameters, or in the detector simulation can be made in these files before starting the simulation.

## Simulating LLP tracks with Delphes

Inside the folder 'delphes_with_tracks' in the Delphes branch are the files of the first atempt to reconstruct the charged parent track using Delphes. All the files need to be added to the modules folder inside Delphes.
