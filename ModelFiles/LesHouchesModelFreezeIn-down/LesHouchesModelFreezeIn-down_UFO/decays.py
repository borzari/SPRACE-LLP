# This file was automatically created by FeynRules 2.3.2
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Sun 1 Apr 2018 17:26:30


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.P__tilde__s0,P.P__tilde__he):'((3*MB**2*yHEbR**2 + 3*mHE**2*yHEbR**2 - 3*ms0**2*yHEbR**2)*cmath.sqrt(MB**4 - 2*MB**2*mHE**2 + mHE**4 - 2*MB**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_c = Decay(name = 'Decay_c',
                particle = P.c,
                partial_widths = {(P.W__plus__,P.s):'(((3*ee**2*MC**2)/(2.*sw**2) + (3*ee**2*MS**2)/(2.*sw**2) + (3*ee**2*MC**4)/(2.*MW**2*sw**2) - (3*ee**2*MC**2*MS**2)/(MW**2*sw**2) + (3*ee**2*MS**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)'})

Decay_d = Decay(name = 'Decay_d',
                particle = P.d,
                partial_widths = {(P.P__tilde__s0,P.P__tilde__he):'((3*MD**2*yHEdR**2 + 3*mHE**2*yHEdR**2 - 3*ms0**2*yHEdR**2)*cmath.sqrt(MD**4 - 2*MD**2*mHE**2 + mHE**4 - 2*MD**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.u):'(((3*ee**2*MD**2)/(2.*sw**2) + (3*ee**2*MU**2)/(2.*sw**2) + (3*ee**2*MD**4)/(2.*MW**2*sw**2) - (3*ee**2*MD**2*MU**2)/(MW**2*sw**2) + (3*ee**2*MU**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.W__minus__,P.ve):'((Me**2 - MW**2)*((ee**2*Me**2)/(2.*sw**2) + (ee**2*Me**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Me)**3)'})

Decay_h = Decay(name = 'Decay_h',
                particle = P.h,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*mh**2*yb**2)*cmath.sqrt(-4*MB**2*mh**2 + mh**4))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.c,P.c__tilde__):'((-12*MC**2*yc**2 + 3*mh**2*yc**2)*cmath.sqrt(-4*MC**2*mh**2 + mh**4))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.d,P.d__tilde__):'((-12*MD**2*ydo**2 + 3*mh**2*ydo**2)*cmath.sqrt(-4*MD**2*mh**2 + mh**4))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.e__minus__,P.e__plus__):'((-4*Me**2*ye**2 + mh**2*ye**2)*cmath.sqrt(-4*Me**2*mh**2 + mh**4))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((mh**2*ym**2 - 4*MMU**2*ym**2)*cmath.sqrt(mh**4 - 4*mh**2*MMU**2))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.s,P.s__tilde__):'((3*mh**2*ys**2 - 12*MS**2*ys**2)*cmath.sqrt(mh**4 - 4*mh**2*MS**2))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.P__tilde__s0,P.P__tilde__s0):'(lams0h**2*vev**2*cmath.sqrt(mh**4 - 4*mh**2*ms0**2))/(8.*cmath.pi*abs(mh)**3)',
                                  (P.t,P.t__tilde__):'((3*mh**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(mh**4 - 4*mh**2*MT**2))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((mh**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(mh**4 - 4*mh**2*MTA**2))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.u,P.u__tilde__):'((3*mh**2*yup**2 - 12*MU**2*yup**2)*cmath.sqrt(mh**4 - 4*mh**2*MU**2))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*mh**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*mh**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(mh**4 - 4*mh**2*MW**2))/(16.*cmath.pi*abs(mh)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*mh**4*vev**2)/(8.*MZ**4) - (3*ee**4*mh**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*mh**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*mh**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*mh**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*mh**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*mh**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*mh**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*mh**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*mh**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(mh**4 - 4*mh**2*MZ**2))/(32.*cmath.pi*abs(mh)**3)'})

Decay_P__tilde__he = Decay(name = 'Decay_P__tilde__he',
                           particle = P.P__tilde__he,
                           partial_widths = {(P.P__tilde__s0,P.b):'((3*MB**2*yHEbR**2 + 3*mHE**2*yHEbR**2 - 3*ms0**2*yHEbR**2)*cmath.sqrt(MB**4 - 2*MB**2*mHE**2 + mHE**4 - 2*MB**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(96.*cmath.pi*abs(mHE)**3)',
                                             (P.P__tilde__s0,P.d):'((3*MD**2*yHEdR**2 + 3*mHE**2*yHEdR**2 - 3*ms0**2*yHEdR**2)*cmath.sqrt(MD**4 - 2*MD**2*mHE**2 + mHE**4 - 2*MD**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(96.*cmath.pi*abs(mHE)**3)',
                                             (P.P__tilde__s0,P.s):'((3*mHE**2*yHEsR**2 + 3*MS**2*yHEsR**2 - 3*ms0**2*yHEsR**2)*cmath.sqrt(mHE**4 - 2*mHE**2*MS**2 + MS**4 - 2*mHE**2*ms0**2 - 2*MS**2*ms0**2 + ms0**4))/(96.*cmath.pi*abs(mHE)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.W__minus__,P.vm):'((MMU**2 - MW**2)*((ee**2*MMU**2)/(2.*sw**2) + (ee**2*MMU**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MMU)**3)'})

Decay_s = Decay(name = 'Decay_s',
                particle = P.s,
                partial_widths = {(P.P__tilde__s0,P.P__tilde__he):'((3*mHE**2*yHEsR**2 + 3*MS**2*yHEsR**2 - 3*ms0**2*yHEsR**2)*cmath.sqrt(mHE**4 - 2*mHE**2*MS**2 + MS**4 - 2*mHE**2*ms0**2 - 2*MS**2*ms0**2 + ms0**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.c):'(((3*ee**2*MC**2)/(2.*sw**2) + (3*ee**2*MS**2)/(2.*sw**2) + (3*ee**2*MC**4)/(2.*MW**2*sw**2) - (3*ee**2*MC**2*MS**2)/(MW**2*sw**2) + (3*ee**2*MS**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)'})

Decay_P__tilde__s0 = Decay(name = 'Decay_P__tilde__s0',
                           particle = P.P__tilde__s0,
                           partial_widths = {(P.b,P.P__tilde__HE):'((-3*MB**2*yHEbR**2 - 3*mHE**2*yHEbR**2 + 3*ms0**2*yHEbR**2)*cmath.sqrt(MB**4 - 2*MB**2*mHE**2 + mHE**4 - 2*MB**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(16.*cmath.pi*abs(ms0)**3)',
                                             (P.d,P.P__tilde__HE):'((-3*MD**2*yHEdR**2 - 3*mHE**2*yHEdR**2 + 3*ms0**2*yHEdR**2)*cmath.sqrt(MD**4 - 2*MD**2*mHE**2 + mHE**4 - 2*MD**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(16.*cmath.pi*abs(ms0)**3)',
                                             (P.P__tilde__he,P.b__tilde__):'((-3*MB**2*yHEbR**2 - 3*mHE**2*yHEbR**2 + 3*ms0**2*yHEbR**2)*cmath.sqrt(MB**4 - 2*MB**2*mHE**2 + mHE**4 - 2*MB**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(16.*cmath.pi*abs(ms0)**3)',
                                             (P.P__tilde__he,P.d__tilde__):'((-3*MD**2*yHEdR**2 - 3*mHE**2*yHEdR**2 + 3*ms0**2*yHEdR**2)*cmath.sqrt(MD**4 - 2*MD**2*mHE**2 + mHE**4 - 2*MD**2*ms0**2 - 2*mHE**2*ms0**2 + ms0**4))/(16.*cmath.pi*abs(ms0)**3)',
                                             (P.P__tilde__he,P.s__tilde__):'((-3*mHE**2*yHEsR**2 - 3*MS**2*yHEsR**2 + 3*ms0**2*yHEsR**2)*cmath.sqrt(mHE**4 - 2*mHE**2*MS**2 + MS**4 - 2*mHE**2*ms0**2 - 2*MS**2*ms0**2 + ms0**4))/(16.*cmath.pi*abs(ms0)**3)',
                                             (P.s,P.P__tilde__HE):'((-3*mHE**2*yHEsR**2 - 3*MS**2*yHEsR**2 + 3*ms0**2*yHEsR**2)*cmath.sqrt(mHE**4 - 2*mHE**2*MS**2 + MS**4 - 2*mHE**2*ms0**2 - 2*MS**2*ms0**2 + ms0**4))/(16.*cmath.pi*abs(ms0)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_u = Decay(name = 'Decay_u',
                particle = P.u,
                partial_widths = {(P.W__plus__,P.d):'(((3*ee**2*MD**2)/(2.*sw**2) + (3*ee**2*MU**2)/(2.*sw**2) + (3*ee**2*MD**4)/(2.*MW**2*sw**2) - (3*ee**2*MD**2*MU**2)/(MW**2*sw**2) + (3*ee**2*MU**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(((-3*ee**2*MC**2)/(2.*sw**2) - (3*ee**2*MS**2)/(2.*sw**2) - (3*ee**2*MC**4)/(2.*MW**2*sw**2) + (3*ee**2*MC**2*MS**2)/(MW**2*sw**2) - (3*ee**2*MS**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(((-3*ee**2*MD**2)/(2.*sw**2) - (3*ee**2*MU**2)/(2.*sw**2) - (3*ee**2*MD**4)/(2.*MW**2*sw**2) + (3*ee**2*MD**2*MU**2)/(MW**2*sw**2) - (3*ee**2*MU**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'((-Me**2 + MW**2)*(-(ee**2*Me**2)/(2.*sw**2) - (ee**2*Me**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MMU**2 + MW**2)*(-(ee**2*MMU**2)/(2.*sw**2) - (ee**2*MMU**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'((-11*ee**2*MC**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MC**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MC**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MC**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'((-7*ee**2*MD**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MD**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MD**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MD**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'((-5*ee**2*Me**2 - ee**2*MZ**2 - (cw**2*ee**2*Me**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*Me**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*Me**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.P__tilde__he,P.P__tilde__HE):'(((8*ee**2*mHE**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*mHE**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MMU**2 - ee**2*MZ**2 - (cw**2*ee**2*MMU**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MMU**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MMU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'((-7*ee**2*MS**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MS**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MS**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MS**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'((-11*ee**2*MU**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MU**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MU**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})
