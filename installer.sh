#!/bin/sh

homeDIR="$( pwd )"

echo "[Checking system dependencies]"
PKG_OK=$(dpkg-query -W -f='${Status}' autoconf 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "autoconf not found. Install it with sudo apt-get install autoconf."
  exit
fi
PKG_OK=$(dpkg-query -W -f='${Status}' libtool 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "libtool not found. Install it with sudo apt-get install libtool."
  exit
fi
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
	echo "[installer] getting MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $madgraph -C MG5 --strip-components 1;
	cd $homeDIR
	rm $madgraph;
	echo "[installer] replacing MadGraph files with fixes";
#    cp ./madgraphfixes/mg5_configuration.txt MG5/input/;
#    cp ./madgraphfixes/madgraph_interface.py MG5/madgraph/interface/;
#    cp ./madgraphfixes/diagram_generation.py MG5/madgraph/core/;

fi

#Get pythia tarball
pythia="pythia8303.tgz"
URL=http://home.thep.lu.se/~torbjorn/pythia8/$pythia
echo -n "Install Pythia (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	if hash gzip 2>/dev/null; then
		mkdir pythia8;
		echo "[installer] getting Pythia"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $pythia -C pythia8 --strip-components 1;
		echo "Installing Pythia in pythia8";
		cd pythia8;
		./configure --with-root=$ROOTSYS --prefix=$homeDIR/pythia8 --with-gzip
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
	echo "[installer] getting Delphes";
  git clone https://github.com/delphes/delphes.git Delphes;
  cd Delphes;
  export PYTHIA8=$homeDIR/pythia8;
  echo "[installer] installing Delphes";
  make HAS_PYTHIA8=true;
	cd $homeDIR;
fi


echo -n "Install CheckMATE (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
  echo "[installer] getting CheckMATE";
  git clone git@github.com:CheckMATE2/checkmate2.git CheckMATE2;
  cd CheckMATE2;
  rm -rf .git
  autoreconf -i -f;
  ./configure --with-rootsys=$ROOTSYS --with-delphes=$homeDIR/Delphes --with-pythia=$homeDIR/pythia8 --with-madgraph=$homeDIR/MG5
  echo "[installer] installing CheckMATE";
  make -j4
       cd $homeDIR
  echo "[installer] Adding new analyses to CheckMATE";
#  cp -r myCheckMateFiles/tools/* CheckMATE2/tools/;
#  cp -r myCheckMateFiles/data/* CheckMATE2/data/;
  cd CheckMATE2;
  echo "[installer] recompiling CheckMATE";
  make;
  cd $homeDIR

fi
