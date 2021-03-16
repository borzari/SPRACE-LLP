# This file was automatically created by FeynRules 2.3.43
# Mathematica version: 12.2.0 for Linux x86 (64-bit) (December 12, 2020)
# Date: Tue 16 Mar 2021 11:14:48


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUS1 = Lorentz(name = 'UUS1',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV++PRIVATE`PYLorentzStrucCounter[{-1, -1, 3}] = Lorentz(name = 'UUV++PRIVATE`PYLorentzStrucCounter[{-1, -1, 3}]',
                                                          spins = [ -1, -1, 3 ],
                                                          structure = 'P(3,2) + P(3,3)')

SSS++PRIVATE`PYLorentzStrucCounter[{1, 1, 1}] = Lorentz(name = 'SSS++PRIVATE`PYLorentzStrucCounter[{1, 1, 1}]',
                                                        spins = [ 1, 1, 1 ],
                                                        structure = '1')

FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}] = Lorentz(name = 'FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}]',
                                                        spins = [ 2, 2, 1 ],
                                                        structure = 'ProjM(2,1)')

FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}] = Lorentz(name = 'FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}]',
                                                        spins = [ 2, 2, 1 ],
                                                        structure = 'ProjM(2,1) - ProjP(2,1)')

FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}] = Lorentz(name = 'FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}]',
                                                        spins = [ 2, 2, 1 ],
                                                        structure = 'ProjP(2,1)')

FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}] = Lorentz(name = 'FFS++PRIVATE`PYLorentzStrucCounter[{2, 2, 1}]',
                                                        spins = [ 2, 2, 1 ],
                                                        structure = 'ProjM(2,1) + ProjP(2,1)')

FFV++PRIVATE`PYLorentzStrucCounter[{2, 2, 3}] = Lorentz(name = 'FFV++PRIVATE`PYLorentzStrucCounter[{2, 2, 3}]',
                                                        spins = [ 2, 2, 3 ],
                                                        structure = '1')

FFV++PRIVATE`PYLorentzStrucCounter[{2, 2, 3}] = Lorentz(name = 'FFV++PRIVATE`PYLorentzStrucCounter[{2, 2, 3}]',
                                                        spins = [ 2, 2, 3 ],
                                                        structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

VSS++PRIVATE`PYLorentzStrucCounter[{3, 1, 1}] = Lorentz(name = 'VSS++PRIVATE`PYLorentzStrucCounter[{3, 1, 1}]',
                                                        spins = [ 3, 1, 1 ],
                                                        structure = 'P(1,2) - P(1,3)')

VVS++PRIVATE`PYLorentzStrucCounter[{3, 3, 1}] = Lorentz(name = 'VVS++PRIVATE`PYLorentzStrucCounter[{3, 3, 1}]',
                                                        spins = [ 3, 3, 1 ],
                                                        structure = 'Metric(1,2)')

VVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3}] = Lorentz(name = 'VVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3}]',
                                                        spins = [ 3, 3, 3 ],
                                                        structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS++PRIVATE`PYLorentzStrucCounter[{1, 1, 1, 1}] = Lorentz(name = 'SSSS++PRIVATE`PYLorentzStrucCounter[{1, 1, 1, 1}]',
                                                            spins = [ 1, 1, 1, 1 ],
                                                            structure = '1')

VVSS++PRIVATE`PYLorentzStrucCounter[{3, 3, 1, 1}] = Lorentz(name = 'VVSS++PRIVATE`PYLorentzStrucCounter[{3, 3, 1, 1}]',
                                                            spins = [ 3, 3, 1, 1 ],
                                                            structure = 'Metric(1,2)')

VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}] = Lorentz(name = 'VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}]',
                                                            spins = [ 3, 3, 3, 3 ],
                                                            structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}] = Lorentz(name = 'VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}]',
                                                            spins = [ 3, 3, 3, 3 ],
                                                            structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}] = Lorentz(name = 'VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}]',
                                                            spins = [ 3, 3, 3, 3 ],
                                                            structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}] = Lorentz(name = 'VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}]',
                                                            spins = [ 3, 3, 3, 3 ],
                                                            structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}] = Lorentz(name = 'VVVV++PRIVATE`PYLorentzStrucCounter[{3, 3, 3, 3}]',
                                                            spins = [ 3, 3, 3, 3 ],
                                                            structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

