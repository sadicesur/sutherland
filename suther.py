#!/usr/bin/env python3

# =============================================================================
# SUTHERLAND VISCOSITY LAW
#
# Author: Sadi Cesur
# E-mail: cesursadi@gmail.com
# Ref.  : William Sutherland (1893) LII. The viscosity of gases and molecular
#         force ,Philosophical Magazine Series 5, 36:223, 507-531, 
#         DOI: 10.1080/14786449308620508
# =============================================================================

# Reference Properties

v_ref = 1.716e-5 # the viscosity in kg/m-s
t_ref = 273.15
s_ref = 110.4 # an effective temperature in K (Sutherland constant)

def suther(temp):
    
    return v_ref * (temp/t_ref)**1.5 * ((t_ref + s_ref)/(temp + s_ref)) 