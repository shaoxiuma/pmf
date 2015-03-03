# -*- coding:utf-8 -*-
"""
The Crop Database holds crop specific parameter. Theses parameter refer to
the requirements of the classes in the Process Library 

:author: Sebastian Multsch

:version: 0.1 (26.10.2010)

:copyright: 
 This program is free software; you can redistribute it and/or modify it under  
 the terms of the GNU General Public License as published by the Free Software  
 Foundation; either version 3 of the License, or (at your option) any later 
 version. This program is distributed in the hope that it will be useful, 
 but WITHOUT ANY  WARRANTY; without even the implied warranty of MERCHANTABILITY 
 or  FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for 
 more details. You should have received a copy of the GNU General 
 Public License along  with this program;
 if not, see <http://www.gnu.org/licenses/>.
"""
class CropCoefficiants_wheat:
    """
    Holds crop specific parameters for summer wheat.
    """
    def __init__(self,
                 stage = [['Emergence',160.],           # end of emergence
                          ['Leaf development',208.],    # end of leaf development
                          ['Tillering',421.],           # end of tillering
                          ['Stem elongation',659.],     # end of stem elongation
                          ['Anthesis',901.],            # end of anthesis
                          ['Seed fill',1174.],          # end of seed fill
                          ['Dough stage',1556.],        # end of dough stage
                          ['Maturity',1665.]],          # end of maturity
                 RUE=3.,            # Stockle 1992 Table1  #RUE=2.2source : Soltani & Sinclair (2012), p.3#RUE at reference CO2 concentration
                 C_0=350.,          # ppm reference atmospheric CO2 concentration
                 factor_b=0.8,      # biomass_lue_soltani
                 b_1 = 7784.,       # biomass_lue_stockle
                 b_2 = 0.00107,     # biomass_lue_stockle
                 R_p = 3.,          # development --> sensitivity to photoperiod
                 photo_on_off = 1., # development --> turning photoperiod response on =1, off =0
                 R_v = 1.5,         # development --> sensitivity to vernalization
                 verna_on_off = 0., # development --> turning vernalization function on =1, off =0
                 w_leafwidth=0.01,  # Shuttelworth-Wallace --> max veg leaf width                 
                 z_0w = 0.005,      # Shuttelworth-Wallace --> Roughness length over weather station ground [m]
                 z_0g = 0.005,      # Shuttelworth-Wallace --> Roughness length of substrate ground [m]
                 z_w = 2.,          # Shuttelworth-Wallace --> Height of weather observation [m]
                 r_st_min = 90.,    # Shuttelworth-Wallace --> Min. stomatal resistance [s m-1]
                 sigma_b = 0.5,     # Shuttelworth-Wallace --> Shielding factor [-]
                 c_int = 0.2,       # Shuttelworth-Wallace --> Interception coefficient [-]
                 k=.4,
                 seasons = [160.0, 499.0, 897.0, 1006.0],  #für baresoil,[0,0,0,0], 
                 kcb = [0.15,1,1,0.15],  #  für baresoil [0,0,0,0],  # für fullcover [1,1,1,1]
                 fact_sen = 50.,     # plant --> leaf --> Factor to adjust senescence rate after maturity
                 FRDR = 0.5,        # plant --> factor changing shape of senescence function [-]
                 min_LAI = 0.1,     # plant --> minimum LAI 
                 max_height = 1.5,  # plant --> max plant height [m]
                 max_depth=150.,    # plant --> max root depth [cm]
                 root_growth=1.5,   # plant --> root growth [cm d-1]
                 leaf_specific_weight = 40.,    # plant --> specific leaf weight (leaf dry mass/projected leaf area) [g m-2]
                 tbase = 0.,        # plant --> min temperature for physiol. processes, needed for temp sum
                 Cr = 0.5,          # netradiation --> extinction coefﬁcient of the vegetation for net radiation
                 albedo_m = 0.2,     # netradiation --> albedo for closed crop canopy (Zhu et al. 2005)
                 CO2_ring=1.1):     # 1.1=ring_A1, 1.2=ring_A2, 1.3=ring_A3, 2.1=ring_E1, 2.2=ring_E2, 2.3=ring_E3 
        self.tbase = tbase
        self.stage=stage
        self.seasons = seasons
        self.factor_b=factor_b
        self.b_1=b_1
        self.b_2=b_2
        self.R_p=R_p    
        self.photo_on_off=photo_on_off
        self.R_v=R_v 
        self.verna_on_off=verna_on_off 
        self.w_leafwidth=w_leafwidth
        self.z_0w=z_0w
        self.z_0g = z_0g
        self.z_w = z_w
        self.r_st_min = r_st_min
        self.sigma_b = sigma_b
        self.c_int = c_int 
        self.k=k
        self.kcb=kcb
        self.RUE=RUE
        self.C_0=C_0
        self.fact_sen=fact_sen
        self.FRDR = FRDR
        self.min_LAI = min_LAI 
        self.max_height = max_height 
        self.max_depth = max_depth
        self.root_growth = root_growth
        self.leaf_specific_weight = leaf_specific_weight
        self.tbase=tbase
        self.Cr = Cr
        self.albedo_m = albedo_m
        self.CO2_ring =CO2_ring
               
               
class CropCoefficiants_c3grass:
    """
    Holds crop specific parameters for C3 grass.
    """        
    def __init__(self,
                 stage = [['Emergence',160.],           # end of emergence
                          ['Leaf development',208.],    # end of leaf development
                          ['Tillering',421.],           # end of tillering
                          ['Stem elongation',659.],     # end of stem elongation
                          ['Anthesis',901.],            # end of anthesis
                          ['Seed fill',1174.],          # end of seed fill
                          ['Dough stage',1556.],        # end of dough stage
                          ['Maturity',1665.]],          # end of maturity
                 RUE=3.,  # tidigare 2.6,           #RUE at reference CO2 concentration
                 C_0=350,           #ppm reference atmospheric CO2 concentration
                 factor_b=0.8,      # biomass_lue_soltani
                 b_1 = 7784.,       # biomass_lue_stockle
                 b_2 = 0.00107,     # biomass_lue_stockle
                 R_p = 3.,          # development --> sensitivity to photoperiod
                 photo_on_off = 1., # development --> turning photoperiod response on =1, off =0
                 R_v = 1.5,         # development --> sensitivity to vernalization
                 verna_on_off = 0., # development --> turning vernalization function on =1, off =0
                 w_leafwidth=0.01,  # Shuttelworth-Wallace --> max veg leaf width                 
                 z_0w = 0.005,      # Shuttelworth-Wallace --> Roughness length over weather station ground [m]
                 z_0g = 0.01,       # Shuttelworth-Wallace --> Roughness length of substrate ground [m]
                 z_w = 2.,          # Shuttelworth-Wallace --> Height of weather observation [m]
                 r_st_min = 115.,   # Shuttelworth-Wallace --> Min. stomatal resistance [s m-1]
                 sigma_b = 0.5,     # Shuttelworth-Wallace --> Shielding factor [-]
                 c_int = 0.2,       # Shuttelworth-Wallace --> Interception coefficient [-]
                 k=.4,
                 seasons = [160.0, 499.0, 897.0, 1006.0],  #für baresoil,[0,0,0,0], 
                 kcb = [0.15,1,1,0.15],  
                 fact_sen = 50.,     # plant --> leaf --> Factor to adjust senescence rate after maturity
                 FRDR = 0.5,        # plant --> factor changing shape of senescence function [-]
                 min_LAI = 0.1,     # plant --> minimum LAI 
                 max_height = 1.,  # plant --> max plant height [m]
                 max_depth=90.,    # plant --> max root depth [cm]
                 root_growth=1.5,   # plant --> root growth [cm d-1]
                 leaf_specific_weight = 40.,    # 40., plant --> specific leaf weight [g m-2]
                 tbase = 1.,#5.,        # plant --> min temperature for physiol. processes, needed for temp sum
                 Cr = 0.5,          # netradiation --> extinction coefﬁcient of the vegetation for net radiation
                 albedo_m = 0.23,  # netradiation --> albedo for closed grass canopy (Zhu et al. 2005)
                 CO2_ring=1.1):     # 1.1=ring_A1, 1.2=ring_A2, 1.3=ring_A3, 2.1=ring_E1, 2.2=ring_E2, 2.3=ring_E3 
        self.tbase = tbase
        self.stage=stage
        self.seasons = seasons
        self.k=k
        self.kcb=kcb
        self.RUE=RUE
        self.factor_b=factor_b
        self.b_1=b_1
        self.b_2=b_2
        self.R_p=R_p    
        self.photo_on_off=photo_on_off
        self.R_v=R_v 
        self.verna_on_off=verna_on_off
        self.w_leafwidth=w_leafwidth
        self.z_0w=z_0w
        self.z_0g = z_0g
        self.z_w = z_w
        self.r_st_min = r_st_min
        self.sigma_b = sigma_b
        self.c_int = c_int      
        self.C_0=C_0
        self.fact_sen=fact_sen        
        self.FRDR = FRDR
        self.min_LAI = min_LAI 
        self.max_height = max_height 
        self.max_depth = max_depth
        self.root_growth = root_growth
        self.leaf_specific_weight = leaf_specific_weight
        self.tbase=tbase
        self.Cr = Cr
        self.albedo_m = albedo_m
        self.CO2_ring =CO2_ring

        
class CropCoefficiants_c4grass:
    """
    Holds crop specific parameters for C4 grass..
    """        
    def __init__(self,
                 stage = [['Emergence',160.],           # end of emergence
                          ['Leaf development',208.],    # end of leaf development
                          ['Tillering',421.],           # end of tillering
                          ['Stem elongation',659.],     # end of stem elongation
                          ['Anthesis',901.],            # end of anthesis
                          ['Seed fill',1174.],          # end of seed fill
                          ['Dough stage',1556.],        # end of dough stage
                          ['Maturity',1665.]],          # end of maturity
                 RUE=3.6,           #RUE at reference CO2 concentration
                 C_0=350,           #ppm reference atmospheric CO2 concentration
                 factor_b=0.4,      # biomass_lue_soltani
                 b_1 = 7784.,       # biomass_lue_stockle
                 b_2 = 0.00107,     # biomass_lue_stockle
                 R_p = 3.,          # development --> sensitivity to photoperiod
                 photo_on_off = 1., # development --> turning photoperiod response on =1, off =0
                 R_v = 1.5,         # development --> sensitivity to vernalization
                 verna_on_off = 0., # development --> turning vernalization function on =1, off =0
                 w_leafwidth=0.01,  # Shuttelworth-Wallace --> max veg leaf width                 
                 z_0w = 0.005,      # Shuttelworth-Wallace --> Roughness length over weather station ground [m]
                 z_0g = 0.01,       # Shuttelworth-Wallace --> Roughness length of substrate ground [m]
                 z_w = 2.,          # Shuttelworth-Wallace --> Height of weather observation [m]
                 r_st_min = 115.,   # Shuttelworth-Wallace --> Min. stomatal resistance [s m-1]
                 sigma_b = 0.5,     # Shuttelworth-Wallace --> Shielding factor [-]
                 c_int = 0.2,       # Shuttelworth-Wallace --> Interception coefficient [-]
                 k=.4,
                 seasons = [160.0, 499.0, 897.0, 1006.0],  #für baresoil,[0,0,0,0], 
                 kcb = [0.15,1,1,0.15],  
                 fact_sen = 50.,     # plant --> leaf --> Factor to adjust senescence rate after maturity
                 FRDR = 0.5,        # plant --> factor changing shape of senescence function [-]
                 min_LAI = 0.1,     # plant --> minimum LAI 
                 max_height = 1.5,  # plant --> max plant height [m]
                 max_depth=150.,    # plant --> max root depth [cm]
                 root_growth=1.5,   # plant --> root growth [cm d-1]
                 leaf_specific_weight = 40.,    # plant --> specific leaf weight [g m-2]
                 tbase = 0.,        # plant --> min temperature for physiol. processes, needed for temp sum
                 Cr = 0.5,          # netradiation --> extinction coefﬁcient of the vegetation for net radiation
                 albedo_m = 0.23,  # netradiation --> albedo for closed grass canopy (Zhu et al. 2005)
                 CO2_ring=1.1):     # 1.1=ring_A1, 1.2=ring_A2, 1.3=ring_A3, 2.1=ring_E1, 2.2=ring_E2, 2.3=ring_E3 
        self.tbase = tbase
        self.stage=stage
        self.seasons = seasons
        self.k=k
        self.kcb=kcb
        self.RUE=RUE
        self.factor_b=factor_b
        self.b_1=b_1
        self.b_2=b_2
        self.R_p=R_p    
        self.photo_on_off=photo_on_off
        self.R_v=R_v 
        self.verna_on_off=verna_on_off
        self.w_leafwidth=w_leafwidth
        self.z_0w=z_0w
        self.z_0g = z_0g
        self.z_w = z_w
        self.r_st_min = r_st_min
        self.sigma_b = sigma_b
        self.c_int = c_int 
        self.C_0=C_0
        self.fact_sen=fact_sen
        self.FRDR = FRDR
        self.min_LAI = min_LAI 
        self.max_height = max_height 
        self.max_depth = max_depth
        self.root_growth = root_growth
        self.leaf_specific_weight = leaf_specific_weight
        self.tbase=tbase
        self.Cr = Cr
        self.albedo_m = albedo_m
        self.CO2_ring =CO2_ring


        

stage = [['sftgs',343.],[],[]]
WW = CropCoefficiants_wheat(stage=stage)