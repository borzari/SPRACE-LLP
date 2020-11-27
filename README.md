# SPRACE-LLP

This repository is being used for studies about Long Lived Particles (LLPs), and sharing codes regarding the simulation of these particles using [MadGraph](https://arxiv.org/abs/1405.0301), [Pythia](https://arxiv.org/abs/1410.3012) and [Delphes](https://arxiv.org/abs/1307.6346) (and CMSSW in the near future).

## Using Madgraph+Pythia+Delphes to simulate LLPs

To run the model described in the paper [LHC-friendly minimal freeze-in models](https://arxiv.org/abs/1811.05478) using Madgraph+Pythia+Delphes, the first step is to download the UFO files available at [http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC](FIMP - UFO). The second step is to move the folder that contain the files to the models folder inside MadGraph. There is a minor change that need to be made in two of those files: the PID of one of the new particles (charged parent) is the same as the one from the neutral pion (111), and MadGraph don't perform the simulation in this case. This need to be changed in the files 'particles.py' and 'parameters.py' to 1000101 (this can essentially be any number above 1000000). The files with the changes are in the folder `UFO_changes`.

After that, you just need to run MadGraph using `/bin/mg5_amc`, import the model `import model Name_of_the_folder`, generate the process of interest (such as `generate p p > ~he ~HE, (~he > l- ~s0), (~HE > l+ ~s0)`, but this depends on the type of the charged parent), use the `output` command to create a folder in which the runs will be saved and `launch` the simulation. Just remember to add the showering/hadronization and the detector simulation packages.

There is a shortcut to all of what was described above that is by using a configuration file that has all the options that need to be active and that will input the necessary commands. Inside the folder `configuration_files` are the files needed to perform this, that should be copied to the MadGraph folder. Notice that the configurations are inside the file `configuration_FIMP_leptons.dat`. The files `param_card_FIMP_lepton.dat`, `run_card_FIMP_lepton.dat` and `delphes_card.dat` are also necessary and any change in the model or the run parameters, or in the detector simulation can be made in these files before starting the simulation. To effectively run the model with the configuration file, just use the command `./bin/mg5_amc configuration_FIMP_leptons.dat`

## Simulating LLP tracks with Delphes

Inside the folder `delphes_with_tracks` are the files of the first atempt to reconstruct the charged parent track using Delphes. All the files need to be added to the modules folder inside Delphes.
