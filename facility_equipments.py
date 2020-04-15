def get_facility_equipments(rlEstabEquipamento, tbEquipamento, tbTipoEquipamento):

    cols_step_0 = ["CO_UNIDADE", "CO_EQUIPAMENTO", "CO_TIPO_EQUIPAMENTO", "QT_EXISTENTE","QT_USO", "DS_EQUIPAMENTO"]
    step0 = rlEstabEquipamento.merge(tbEquipamento, 
                                    on=["CO_EQUIPAMENTO", "CO_TIPO_EQUIPAMENTO"], 
                                    validate="many_to_one")[cols_step_0]

    cols_step_1 = ["CO_UNIDADE","DS_TIPO_EQUIPAMENTO", "DS_EQUIPAMENTO", "QT_EXISTENTE", "QT_USO"]
    step1 = step0.merge(tbTipoEquipamento, on="CO_TIPO_EQUIPAMENTO", validate="many_to_one")[cols_step_1]

    facility_equipments = step1.copy()

    return facility_equipments