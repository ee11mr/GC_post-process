# EQUATIOONS FROM gckpp_Rates
def GCARR(A0, B0, C0, T):
    return A0 * np.exp(C0/T) * (300./T)**B0
    
def GCJPLPR(A0, B0, C0, A1, B1, C1, FV, T, NUMDEN):
    RLOW  = GCARR(A0, B0, C0 , T) * NUMDEN
    RHIGH = GCARR(A1, B1, C1 , T)
    XYRAT = RLOW/RHIGH
    BLOG  = np.log10(XYRAT)
    FEXP  = 1. / (1. + BLOG * BLOG)
    return RLOW * FV**FEXP / (1.+XYRAT)
    
def ISO1(A0, B0, C0, D0, E0, F0, G0, T):
    K0 = D0*np.exp(E0/T)*np.exp(1.E8/T**3)
    K1 = F0*np.exp(G0/T)
    K2 = C0*K0/(K0+K1)
    return A0 * np.exp(B0/T) * (1.-K2)
    
def ISO2(A0, B0, C0, D0, E0, F0, G0, T):
     K0 = D0*np.exp(E0/T)*np.exp(1.E8/T**3)
     K1 = F0*np.exp(G0/T)
     K2 = C0*K0/(K0+K1)
     return A0 * np.exp(B0/T) * K2
     
def GC_OHHNO3(A0, B0, C0, A1, B1, C1, A2, B2, C2, T, NUMDEN):
    R0 =  A0 * np.exp(C0/T) * (300/T)**B0
    R1 =  A1 * np.exp(C1/T) * (300/T)**B1
    R2 =  NUMDEN*(A2 * np.exp(C2/T) * (300/T)**B2)
    return R0 + R2/(1. + R2/R1)
    
def EPO(A1, E1, M1, T, NUMDEN):     
     K1 = 1.0/(M1 * NUMDEN + 1.0)
     return A1 * np.exp(E1/T) *  K1    
    
def TOTAL_OH_REACT_calc(model):
    #REPLACE WITH AIR DEN WHEN DONE
    model["PRPE_REACT"]   = model["concAfterChem_PRPE"]  * GCJPLPR(4.60E-27, 4.0E+00, 0.0, 2.6E-11, 1.3,    0.0, 0.5, model["Met_T"], 2.69e19)
    model["C2H4_REACT"]   = model["concAfterChem_C2H4"]  * GCJPLPR(1.00E-28, 4.5E+00, 0.0, 8.8E-12, 8.5E-1, 0.0, 0.6, model["Met_T"], 2.69e19)
    model["NO2_REACT"]    = model["concAfterChem_NO2"]   * GCJPLPR(1.80E-30, 3.0E+00, 0.0, 2.8E-11, 0.0,    0.0, 0.6, model["Met_T"], 2.69e19)
    model["NO_REACT"]     = model["concAfterChem_NO"]    * GCJPLPR(7.00E-31, 2.6E+00, 0.0, 3.6E-11, 0.1,    0.0, 0.6, model["Met_T"], 2.69e19)
    model["ISOP_REACT"]   =  model["concAfterChem_ISOP"] * ISO1(1.7E-11, 390.0, 9.33E-2, 5.05E15, -12200.0, 1.79E14, -8830.0, model["Met_T"])
    model["ISOP_REACT"]  += model["concAfterChem_ISOP"]  * ISO1(1.0E-11, 390.0, 2.26E-1, 2.22E9,  -7160.0,  1.75E14, -9054.0, model["Met_T"])
    model["ISOP_REACT"]  += model["concAfterChem_ISOP"]  * ISO2(1.7E-11, 390.0, 9.33E-2, 5.05E15, -12200.0, 1.79E14, -8830.0, model["Met_T"])
    model["ISOP_REACT"]  += model["concAfterChem_ISOP"]  * ISO2(1.0E-11, 390.0, 2.26E-1, 2.22E9,  -7160.0,  1.75E14, -9054.0, model["Met_T"])
    model["AROM_REACT"]   = model["concAfterChem_AROM"]  * GCARR(1.75E-11,  0.0E+00, 0.0,    model["Met_T"])
    model["TMB_REACT"]    =  model["concAfterChem_TMB"]  * GCARR(4.27e-11,  0.0E+00, 0.0,    model["Met_T"])
    model["XYLE_REACT"]   = model["concAfterChem_XYLE"]  * GCARR(2.13e-11,  0.0E+00, 0.0,    model["Met_T"])
    model["XYLO_REACT"]   = model["concAfterChem_XYLO"]  * GCARR(1.37e-11,  0.0E+00, 0.0,    model["Met_T"])
    model["TOLU_REACT"]   = model["concAfterChem_TOLU"]  * GCARR(1.81E-12,  0.0E+00, 354.0,  model["Met_T"])
    model["BENZ_REACT"]   = model["concAfterChem_BENZ"]  * GCARR(2.33E-12,  0.0E+00, -193.0, model["Met_T"])
    model["C3H8_REACT"]   = model["concAfterChem_C3H8"]  * GCARR(7.60E-12, 0.0E+00, -585.0,  model["Met_T"])
    model["C2H6_REACT"]   = model["concAfterChem_C2H6"]  * GCARR(7.66E-12, 0.0E+00, -1020.0, model["Met_T"])
    model["O3_REACT"]     = model["concAfterChem_O3"]    * GCARR(1.70E-12, 0.0E+00, -940.0,  model["Met_T"])
    model["HO2_REACT"]    = model["concAfterChem_HO2"]   * GCARR(4.80E-11, 0.0E+00,  250.0,  model["Met_T"])
    model["H2_REACT"]     = model["concAfterChem_H2"]    * GCARR(2.80E-12, 0.0E+00, -1800.0, model["Met_T"])
    model["CO_REACT"]     = model["concAfterChem_CO"]    * GCARR(1.50E-13, 0.0E+00,  0.0,    model["Met_T"])
    model["CH2O_REACT"]   = model["concAfterChem_CH2O"]  * GCARR(5.50E-12, 0.0E+00, 125.0,   model["Met_T"])
    model["ALK4_REACT"]   = model["concAfterChem_ALK4"]  * GCARR(9.10E-12, 0.0E+00, -405.0,  model["Met_T"])
    model["ALD2_REACT"]   = model["concAfterChem_ALD2"]  * GCARR(4.63E-12, 0.0E+00, 350.0,   model["Met_T"])
    model["ACET_REACT"]   = model["concAfterChem_ACET"]  * (1.33E-13+3.82E-11*np.exp(-2000.0/model["Met_T"]))
    model["HNO2_REACT"]   = model["concAfterChem_HNO2"]  * GCARR(1.80E-11, 0.0E+00, -390.0,  model["Met_T"])
    model["MEK_REACT"]    = model["concAfterChem_MEK"]   * GCARR(1.30E-12, 0.0E+00, -25.0,   model["Met_T"])
    model["RCHO_REACT"]   = model["concAfterChem_RCHO"]  * GCARR(6.00E-12, 0.0E+00, 410.0,   model["Met_T"])
    model["CH4_REACT"]    = model["concAfterChem_CH4"]   * GCARR(2.45E-12, 0.0E+00, -1775.0, model["Met_T"])
    model["MVK_REACT"]    = model["concAfterChem_MVK"]   * GCARR(2.60E-12, 0.0E+00, 610.0,   model["Met_T"])
    model["MACR_REACT"]   = model["concAfterChem_MACR"]  * GCARR(4.40E-12, 0.0E+00, 380.0,   model["Met_T"])
    model["MACR_REACT"]  += model["concAfterChem_MACR"]  * GCARR(2.70E-12, 0.0E+00, 470.0,   model["Met_T"])
    model["R4N2_REACT"]   = model["concAfterChem_R4N2"]  * GCARR(1.60E-12, 0.0E+00, 0.0,     model["Met_T"])
    model["MP_REACT"]     = model["concAfterChem_MP"]    * GCARR(2.66E-12, 0.0E+00, 200.0,   model["Met_T"])
    model["MP_REACT"]    += model["concAfterChem_MP"]    * GCARR(1.14E-12, 0.0E+00, 200.0,   model["Met_T"])
    model["PHEN_REACT"]   = model["concAfterChem_PHEN"]  * GCARR(6.75E-12, 0.0E+00, 405.0,   model["Met_T"])
    model["CSL_REACT"]    = model["concAfterChem_CSL"]   * GCARR(4.65E-11, 0.0E+00, 0.0,     model["Met_T"])
    model["OH_REACT"]     = model["concAfterChem_OH"]    * GCARR(1.80E-12, 0.0E+00, 0.0,     model["Met_T"])
    model["OH_REACT"]    += model["concAfterChem_OH"]    * GCJPLPR(6.90E-31, 1.0E+00, 0.0, 2.6E-11, 0.0, 0.0, 0.6, model["Met_T"], 2.69e19)
    model["H2O2_REACT"]   = model["concAfterChem_H2O2"]  * GCARR(1.80E-12, 0.0E+00, 0.0,     model["Met_T"])
    model["ATOOH_REACT"]  = model["concAfterChem_ATOOH"] * GCARR(2.66E-12, 0.0E+00, 200.0,   model["Met_T"])
    model["ATOOH_REACT"] += model["concAfterChem_ATOOH"] * GCARR(1.14E-12, 0.0E+00, 200.0,   model["Met_T"])
    model["HNO3_REACT"]   = model["concAfterChem_HNO3"]  * GC_OHHNO3(2.41E-14, 0.0E+00, 460.0, 2.69E-17, 0.E0, 2199., 6.51E-34, 0.E0, 1335.0, model["Met_T"], 2.69e19)
    model["HNO4_REACT"]   = model["concAfterChem_HNO4"]  * GCARR(1.30E-12, 0.0E+00, 380.0,  model["Met_T"])
    model["MOH_REACT"]    = model["concAfterChem_MOH"]   * GCARR(2.90E-12, 0.0E+00, -345.0, model["Met_T"])
    model["EOH_REACT"]    = model["concAfterChem_EOH"]   * GCARR(3.35E-12, 0.0E+00, 0.0,    model["Met_T"])
    model["NO3_REACT"]    = model["concAfterChem_NO3"]   * GCARR(2.20E-11, 0.0E+00, 0.0,    model["Met_T"])
    model["HCOOH_REACT"]  = model["concAfterChem_HCOOH"] * GCARR(4.00E-13, 0.0E+00, 0.0,    model["Met_T"])
    model["ACTA_REACT"]   = model["concAfterChem_ACTA"]  * GCARR(3.15E-14, 0.0E+00, 920.0,  model["Met_T"])
    model["ROH_REACT"]    = model["concAfterChem_ROH"]   * GCARR(4.60E-12, 0.0E+00, 70.0,   model["Met_T"])
    model["GLYC_REACT"]   = model["concAfterChem_GLYC"]  * GCARR(8.00E-12, 0.0E+00, 0.0,    model["Met_T"])
    model["GLYC_REACT"]  += model["concAfterChem_GLYC"]  * GCARR(8.00E-12, 0.0E+00, 0.0,    model["Met_T"])
    model["GLYX_REACT"]   = model["concAfterChem_GLYX"]  * GCARR(3.10E-12, 0.0E+00, 340.0,  model["Met_T"])
    model["MGLY_REACT"]   = model["concAfterChem_MGLY"]  * GCARR(1.50E-11, 0.0E+00, 0.0,    model["Met_T"])
    model["HAC_REACT"]    = model["concAfterChem_HAC"]   * GCARR(2.15E-12, 0.0E+00, 305.0,  model["Met_T"])
    model["HAC_REACT"]   += model["concAfterChem_HAC"]   * GCARR(2.15E-12, 0.0E+00, 305.0,  model["Met_T"])
    model["PRPN_REACT"]   = model["concAfterChem_PRPN"]  * GCARR(8.78E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["ETP_REACT"]    = model["concAfterChem_ETP"]   * GCARR(5.18E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["RA3P_REACT"]   = model["concAfterChem_RA3P"]  * GCARR(5.18E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["RB3P_REACT"]   = model["concAfterChem_RB3P"]  * GCARR(8.78E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["R4P_REACT"]    = model["concAfterChem_R4P"]   * GCARR(8.78E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["RP_REACT"]     = model["concAfterChem_RP"]    * GCARR(6.13E-13, 0.0E+00, 200.0,  model["Met_T"])
    model["PP_REACT"]     = model["concAfterChem_PP"]    * GCARR(8.78E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["LVOC_REACT"]   = model["concAfterChem_LVOC"]  * GCARR(4.82E-11, 0.0E+00, -400.0,  model["Met_T"])
    model["MAP_REACT"]    = model["concAfterChem_MAP"]   * GCARR(6.13E-13, 0.0E+00, 200.0,  model["Met_T"])
    model["DMS_REACT"]    = model["concAfterChem_DMS"]   * GCARR(1.20E-11, 0.0E+00, -280.0,  model["Met_T"])
    model["SO2_REACT"]    = model["concAfterChem_SO2"]   * GCJPLPR(3.30E-31, 4.3E+00, 0.0, 1.6E-12, 0.0, 0.0, 0.6, model["Met_T"], 2.69e19)
    model["HBr_REACT"]    = model["concAfterChem_HBr"]   * GCARR(5.50E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["Br2_REACT"]    = model["concAfterChem_Br2"]   * GCARR(2.10E-11, 0.0E+00, 240.0,  model["Met_T"])
    model["BrO_REACT"]    = model["concAfterChem_BrO"]   * GCARR(1.70E-11, 0.0E+00, 250.0,  model["Met_T"])
    model["CHBr3_REACT"]  = model["concAfterChem_CHBr3"] * GCARR(9.00E-13, 0.0E+00, -360.0,  model["Met_T"])
    model["CH2Br2_REACT"] = model["concAfterChem_CH2Br2"]* GCARR(2.00E-12, 0.0E+00, -840.0,  model["Met_T"])
    model["CH3Br_REACT"]  = model["concAfterChem_CH3Br"] * GCARR(1.42E-12, 0.0E+00, -1150.0,  model["Met_T"])
    model["ClO_REACT"]    = model["concAfterChem_ClO"]   * GCARR(7.40E-12, 0.0E+00, 270.0,  model["Met_T"])
    model["ClO_REACT"]   += model["concAfterChem_ClO"]   * GCARR(6.00E-13, 0.0E+00, 230.0,  model["Met_T"])
    model["OClO_REACT"]   = model["concAfterChem_OClO"]  * GCARR(1.40E-12, 0.0E+00, 600.0,  model["Met_T"])
    model["Cl2O2_REACT"]  = model["concAfterChem_Cl2O2"] * GCARR(6.00E-13, 0.0E+00, 670.0,  model["Met_T"])
    model["HCl_REACT"]    = model["concAfterChem_HCl"]   * GCARR(1.80E-12, 0.0E+00, -250.0,  model["Met_T"])
    model["HOCl_REACT"]   = model["concAfterChem_HOCl"]  * GCARR(3.00E-12, 0.0E+00, -500.0,  model["Met_T"])
    model["ClNO2_REACT"]  = model["concAfterChem_ClNO2"] * GCARR(2.40E-12, 0.0E+00, -1250.0,  model["Met_T"])
    model["ClNO3_REACT"]  = model["concAfterChem_ClNO3"] * GCARR(1.20E-12, 0.0E+00, -330.0,  model["Met_T"])
    model["CH3Cl_REACT"]  = model["concAfterChem_CH3Cl"] * GCARR(1.96E-12, 0.0E+00, -1200.0,  model["Met_T"])
    model["CH2Cl2_REACT"] = model["concAfterChem_CH2Cl2"]* GCARR(2.61E-12, 0.0E+00, -944.0,  model["Met_T"])
    model["CHCl3_REACT"]  = model["concAfterChem_CHCl3"] * GCARR(4.69E-12, 0.0E+00, -1134.0,  model["Met_T"])
    model["I2_REACT"]     = model["concAfterChem_I2"]    * GCARR(1.80E-10, 0.0E+00, 0.0,  model["Met_T"])
    model["HI_REACT"]     = model["concAfterChem_HI"]    * GCARR(3.00E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["HOI_REACT"]    = model["concAfterChem_HOI"]   * GCARR(5.00E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["CH3I_REACT"]   = model["concAfterChem_CH3I"]  * GCARR(2.90E-12, 0.0E+00, -1100.0,  model["Met_T"])
    model["ETHLN_REACT"]  = model["concAfterChem_ETHLN"] * GCARR(2.40E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["PROPNN_REACT"] = model["concAfterChem_PROPNN"]* GCARR(6.70E-13, 0.0E+00, 0.0,  model["Met_T"])
    model["MTPA_REACT"]   = model["concAfterChem_MTPA"]  * GCARR(1.21E-11, 0.0E+00, 440.0,  model["Met_T"])
    model["MTPO_REACT"]   = model["concAfterChem_MTPO"]  * GCARR(1.21E-11, 0.0E+00, 440.0,  model["Met_T"])
    model["LIMO_REACT"]   = model["concAfterChem_LIMO"]  * GCARR(4.20E-11, 0.0E+00, 401.0,  model["Met_T"])
    model["PIP_REACT"]    = model["concAfterChem_PIP"]   * GCARR(3.40E-12, 0.0E+00, 190.0,  model["Met_T"])
    model["MONITS_REACT"] = model["concAfterChem_MONITS"]* GCARR(4.80E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["MONITU_REACT"] = model["concAfterChem_MONITU"]* GCARR(7.29E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["HONIT_REACT"]  = model["concAfterChem_HONIT"] * GC_OHHNO3(2.41E-14, 0.0E+00, 460.0, 2.69E-17, 0.E0, 2199.0, 6.51E-34, 0.E0, 1335.0, model["Met_T"], 2.69e19)
    model["MENO3_REACT"]  = model["concAfterChem_MENO3"] * GCARR(8.00E-13, 0.0E+00, -1000.0,  model["Met_T"])
    model["ETNO3_REACT"]  = model["concAfterChem_ETNO3"] * GCARR(1.00E-12, 0.0E+00, -490.0,  model["Met_T"])
    model["IPRNO3_REACT"] = model["concAfterChem_IPRNO3"]* GCARR(1.20E-12, 0.0E+00, -320.0,  model["Met_T"])
    model["NPRNO3_REACT"] = model["concAfterChem_NPRNO3"]* GCARR(7.10E-13, 0.0E+00, 0.0,  model["Met_T"])
    model["HPALD1_REACT"] = model["concAfterChem_HPALD1"]* GCARR(1.17E-11, 0.0E+00, 450.0,  model["Met_T"])
    model["HPALD2_REACT"] = model["concAfterChem_HPALD2"]* GCARR(1.17E-11, 0.0E+00, 450.0,  model["Met_T"])
    model["HPALD3_REACT"] = model["concAfterChem_HPALD3"]* GCARR(2.20E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["HPALD4_REACT"] = model["concAfterChem_HPALD4"]* GCARR(3.50E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["HC5A_REACT"]   = model["concAfterChem_HC5A"]  * GCARR(4.64E-12, 0.0E+00, 650.0,  model["Met_T"])
    model["ICHE_REACT"]   = model["concAfterChem_ICHE"]  * GCARR(9.85E-12, 0.0E+00, 410.0,  model["Met_T"])
    model["IDC_REACT"]    = model["concAfterChem_IDC"]   * GCARR(3.00E-12, 0.0E+00, 650.0,  model["Met_T"])
    model["RIPA_REACT"]   = model["concAfterChem_RIPA"]  * GCARR(2.47E-12, 0.0E+00, 390.0,  model["Met_T"])
    model["RIPA_REACT"]  += model["concAfterChem_RIPA"]  * GCARR(6.10E-12, 0.0E+00, 200.0,  model["Met_T"]) 
    model["RIPA_REACT"]  += model["concAfterChem_RIPA"]  * EPO(1.62E-11, 390.0, 4.77E-21, model["Met_T"], 2.69e19)
    model["RIPB_REACT"]   = model["concAfterChem_RIPB"]  * GCARR(4.35E-12, 0.0E+00, 390.0,  model["Met_T"])
    model["RIPB_REACT"]  += model["concAfterChem_RIPB"]  * GCARR(4.10E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["RIPB_REACT"]  += model["concAfterChem_RIPB"]  * EPO(2.85E-11, 390.0, 4.77E-21, model["Met_T"], 2.69e19)
    model["RIPC_REACT"]   = model["concAfterChem_RIPC"]  * GCARR(3.53E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["RIPD_REACT"]   = model["concAfterChem_RIPD"]  * GCARR(3.53E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["IEPOXD_REACT"] = model["concAfterChem_IEPOXD"]* GCARR(3.22E-11, 0.0E+00, -400.0,  model["Met_T"])
    model["IEPOXA_REACT"] = model["concAfterChem_IEPOXA"]* GCARR(1.05E-11, 0.0E+00, -400.0,  model["Met_T"])
    model["IEPOXA_REACT"]+= model["concAfterChem_IEPOXA"]* EPO(5.82E-11, -400.0, 1.14E-20, model["Met_T"], 2.69e19)
    model["IEPOXB_REACT"] = model["concAfterChem_IEPOXB"]* GCARR(8.25E-12, 0.0E+00, -400.0,  model["Met_T"])
    model["IEPOXB_REACT"]+= model["concAfterChem_IEPOXB"]* EPO(3.75E-11, -400.0, 8.91E-21, model["Met_T"], 2.69e19)  
    model["IHN2_REACT"]   = model["concAfterChem_IHN2"]  * GCARR(7.14E-12, 0.0E+00, 390.0,  model["Met_T"])
    model["IHN2_REACT"]  += model["concAfterChem_IHN2"]  * EPO(6.30E-12, 390.0, 1.62E-191, model["Met_T"], 2.69e19)
    model["IHN3_REACT"]   = model["concAfterChem_IHN3"]  * GCARR(1.02E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["IHN3_REACT"]  += model["concAfterChem_IHN3"]  * EPO(1.05E-11, 390.0, 2.49E-19, model["Met_T"], 2.69e19)
    model["IHN1_REACT"]   = model["concAfterChem_IHN1"]  * GCARR(2.04E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["IHN1_REACT"]  += model["concAfterChem_IHN1"]  * EPO(1.55E-11, 390.0, 2.715E-19, model["Met_T"], 2.69e19)
    model["IHN4_REACT"]   = model["concAfterChem_IHN4"]  * GCARR(2.95E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["IHN4_REACT"]  += model["concAfterChem_IHN4"]  * EPO(9.52E-12, 390.0, 2.715E-19, model["Met_T"], 2.69e19)
    model["INPB_REACT"]   = model["concAfterChem_INPB"]  * GCARR(5.88E-12, 0.0E+00, 390.0,  model["Met_T"])
    model["INPB_REACT"]  += model["concAfterChem_INPB"]  * EPO(4.471E-12, 390.0, 2.28E-20, model["Met_T"], 2.69e19)
    model["INPB_REACT"]  += model["concAfterChem_INPB"]  * GCARR(2.278E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["INPD_REACT"]   = model["concAfterChem_INPD"]  * GCARR(1.61E-11, 0.0E+00, 390.0,  model["Met_T"])
    model["INPD_REACT"]  += model["concAfterChem_INPD"]  * EPO(8.77E-12,390.0,2.185E-20, model["Met_T"], 2.69e19)
    model["INPD_REACT"]  += model["concAfterChem_INPD"]  * EPO(1.493E-11,390.0,2.715E-19, model["Met_T"], 2.69e19)
    model["INPD_REACT"]  += model["concAfterChem_INPD"]  * GCARR(3.40E-12, 0.0E+00, 200.0,  model["Met_T"])
    model["INPD_REACT"]  += model["concAfterChem_INPD"]  * GCARR(7.50E-12, 0.0E+00, 20.0,  model["Met_T"])
    model["ICN_REACT"]    = model["concAfterChem_ICN"]   * GCARR(9.35E-12, 0.0E+00, 390.0,  model["Met_T"])
    model["ICN_REACT"]   += model["concAfterChem_ICN"]   * EPO(2.97E-12, 390.0, 2.715E-19, model["Met_T"], 2.69e19)
    model["IDN_REACT"]    = model["concAfterChem_IDN"]   * GCARR(1.00E-11, 0.0E+00, 0.0,  model["Met_T"]) 
    model["MVKN_REACT"]   = model["concAfterChem_MVKN"]  * GCARR(1.24E-12, 0.0E+00, 380.0,  model["Met_T"])
    model["MVKHP_REACT"]  = model["concAfterChem_MVKHP"] * GCARR(5.77E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["MCRHP_REACT"]  = model["concAfterChem_MCRHP"] * GCARR(2.70E-12, 0.0E+00, 470.0,  model["Met_T"])
    model["MCRHN_REACT"]  = model["concAfterChem_MCRHN"] * GCARR(1.39E-11, 0.0E+00, 380.0,  model["Met_T"])
    model["MCRHNB_REACT"] = model["concAfterChem_MCRHNB"]* GCARR(2.70E-12, 0.0E+00, 470.0,  model["Met_T"]) 
    model["MCRENOL_REACT"]= model["concAfterChem_MCRENOL"]* GCARR(3.71E-12, 0.0E+00, 983.0,  model["Met_T"])
    model["MVKPC_REACT"]  = model["concAfterChem_MVKPC"] * GCARR(5.00E-12, 0.0E+00, 470.0,  model["Met_T"])
    model["MVKDH_REACT"]  = model["concAfterChem_MVKDH"] * GCARR(8.70E-12, 0.0E+00, 70.0,  model["Met_T"])
    model["MVKHCB_REACT"] = model["concAfterChem_MVKHCB"]* GCARR(5.00E-12, 0.0E+00, 470.0,  model["Met_T"])
    model["MVKHC_REACT"]  = model["concAfterChem_MVKHC"] * GCARR(2.00E-12, 0.0E+00, 70.0,  model["Met_T"])
    model["MCRDH_REACT"]  = model["concAfterChem_MCRDH"] * GCARR(2.4E-11, 0.0E+00, 70.0,  model["Met_T"])
    model["MACR1OOH_REACT"]= model["concAfterChem_MACR1OOH"]* GCARR(1.66E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["MPAN_REACT"]   = model["concAfterChem_MPAN"]  * GCARR(2.90E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["HMML_REACT"]   = model["concAfterChem_HMML"]  * GCARR(4.33E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["ICPDH_REACT"]  = model["concAfterChem_ICPDH"] * GCARR(1.00E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["IDCHP_REACT"]  = model["concAfterChem_IDCHP"] * GCARR(2.25E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["IDHDP_REACT"]  = model["concAfterChem_IDHDP"] * GCARR(3.00E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["IDHPE_REACT"]  = model["concAfterChem_IDHPE"] * GCARR(3.00E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["ITCN_REACT"]   = model["concAfterChem_ITCN"]  * GCARR(1.00E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["ITHN_REACT"]   = model["concAfterChem_ITHN"]  * GCARR(3.00E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["PYAC_REACT"]   = model["concAfterChem_PYAC"]  * GCARR(8.00E-13, 0.0E+00, 0.0,  model["Met_T"])
    model["HMHP_REACT"]   = model["concAfterChem_HMHP"]  * GCARR(1.30E-12, 0.0E+00, 0.0,  model["Met_T"])
    model["HPETHNL_REACT"]= model["concAfterChem_HPETHNL"]* GCARR(1.55E-12, 0.0E+00, 340.0,  model["Met_T"])
    model["HPETHNL_REACT"]= model["concAfterChem_HPETHNL"]* GCARR(2.91E-11, 0.0E+00, 0.0,  model["Met_T"])
    model["DCB2_REACT"]   = model["concAfterChem_DCB2"]  * GCARR(2.8E-11, 0.0E+00, 175.0,  model["Met_T"])
    model["DCB1_REACT"]   = model["concAfterChem_DCB1"]  * GCARR(2.8E-11, 0.0E+00, 175.0,  model["Met_T"])
    model["DCB3_REACT"]   = model["concAfterChem_DCB3"]  * GCARR(1.0E-13, 0.0E+00, 0.0,  model["Met_T"])
    model["MCT_REACT"]    = model["concAfterChem_MCT"]   * GCARR(2.05E-10, 0.0E+00, 0.0,  model["Met_T"])
    model["EPX_REACT"]    = model["concAfterChem_EPX"]   * GCARR(2.80E-11, 0.0E+00, 175.0,  model["Met_T"])
    model["ETEG_REACT"]   = model["concAfterChem_ETEG"]  * GCARR(1.47E-11, 0.0E+00, 0.0,  model["Met_T"])
    
    #model["_REACT"] = model["concAfterChem_"]* GCARR(,  model["Met_T"])
    
    model["TOTAL_OH_REACT"]   = model[[x for x in model.columns if "REACT" in x]].sum(axis=1)     
    return model["TOTAL_OH_REACT"]   