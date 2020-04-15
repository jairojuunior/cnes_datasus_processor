def get_facility_infrastructure(rlEstabInstFisiAssist, tbInstalFisicaParaAssist):
    cols_step_0 = ["CO_UNIDADE", "DS_INSTALACAO", "QT_INSTALACAO", "NU_LEITOS"]
    step0  = rlEstabInstFisiAssist.merge(tbInstalFisicaParaAssist, on=["CO_INSTALACAO"], 
                                        validate="many_to_one")[cols_step_0]
    facility_infrastructure = step0.copy()
    
    return facility_infrastructure