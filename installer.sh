#!/bin/sh

homeDIR="$( pwd )"


PKG_OK=$(dpkg-query -W -f='${Status}' gzip 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "gzip not found. Install it with sudo apt-get install gzip."
  exit
fi


madgraph="MG5_aMC_v2.8.2.tar.gz"
URL=https://launchpad.net/mg5amcnlo/2.0/2.8.x/+download/$madgraph
echo -n "Install MadGraph (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir MG5;
	echo "[installer] fetching MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $madgraph -C MG5 --strip-components 1;
	cd $homeDIR
	rm $madgraph;
#	echo "[installer] replacing MadGraph files with fixes";
#    cp ./madgraphfixes/mg5_configuration.txt MG5/input/;
#    cp ./madgraphfixes/madgraph_interface.py MG5/madgraph/interface/;
fi

#Get FastJet tarball
fastjet="fastjet-3.3.4"
URL=http://fastjet.fr/repo/$fastjet.tar.gz
echo -n "Install FastJet (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir fastjet_tmp
	echo "[installer] fetching Fastjet"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $fastjet.tar.gz -C fastjet_tmp;
	mkdir $fastjet;
	echo "Installing Fastjet in $fastjet";
	cd fastjet_tmp/$fastjet;
	./configure  --enable-allplugins --prefix=$homeDIR/$fastjet/;
	make install;

	#Clean up
	cd $homeDIR
	rm -rf fastjet_tmp; rm $fastjet.tar.gz;
fi

#Get HepMC tarball
hepmc="hepmc2.06.11"
echo -n "Install HepMC (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir hepMC_tmp
	URL=http://hepmc.web.cern.ch/hepmc/releases/$hepmc.tgz
	echo "[installer] getting HepMC"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $hepmc.tgz -C hepMC_tmp --strip-components 1;
	mkdir $hepmc; mkdir $hepmc/build; mkdir HepMC;
	echo "Installing HepMC in ./HepMC";
	cd $hepmc/build;
	../../hepMC_tmp/configure --prefix=$homeDIR/HepMC --with-momentum=GEV --with-length=MM;
	make;
	make check;
	make install;

	#Clean up
	cd $homeDIR;
	rm -rf hepMC_tmp; rm $hepmc.tgz;
fi


#Get pythia tarball
pythia="pythia8303.tgz"
URL=http://home.thep.lu.se/~torbjorn/pythia8/$pythia
echo -n "Install Pythia (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	if hash gzip 2>/dev/null; then
		mkdir pythia8;
		echo "[installer] fetching Pythia"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $pythia -C pythia8 --strip-components 1;
		echo "Installing Pythia in pythia8";
		cd pythia8;
		./configure --with-root=$ROOTSYS --prefix=$homeDIR/pythia8 --with-gzip --with-fastjet3=../$fastjet --with-hepmc2=$homeDIR/HepMC
		make -j4; make install;
		cd $homeDIR
		rm $pythia;
	else
		echo "[installer] gzip is required. Try to install it with sudo apt-get install gzip";
	fi
fi

echo -n "Install Delphes (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	echo "[installer] fetching Delphes";
  git clone https://github.com/delphes/delphes.git Delphes;
  cd Delphes;
  echo "[installer] installing Delphes";
  make -j4;
	cd $homeDIR;
fi

