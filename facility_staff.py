def get_facility_staff(tbCargaHorariaSus, tbAtividadeProfissional):

    cols_step_0 = ["CO_UNIDADE", "DS_ATIVIDADE_PROFISSIONAL", "CO_PROFISSIONAL_SUS", "QT_CARGA_HORARIA_AMBULATORIAL"]
    step0 = tbCargaHorariaSus.merge(tbAtividadeProfissional, on=["CO_CBO"],
                                    validate="many_to_one")[cols_step_0]

    step1 = step0.groupby(["CO_UNIDADE", "DS_ATIVIDADE_PROFISSIONAL"])["QT_CARGA_HORARIA_AMBULATORIAL"].sum().reset_index()
    step1.rename(columns={"QT_CARGA_HORARIA_AMBULATORIAL": "SUM_HOURS"}, inplace=True)

    step2 = step0.groupby(["CO_UNIDADE", "DS_ATIVIDADE_PROFISSIONAL"]).count().reset_index()
    step2.drop("QT_CARGA_HORARIA_AMBULATORIAL", axis=1, inplace=True)
    step2.rename(columns={"CO_PROFISSIONAL_SUS": "QTY_SUS_STAFF"}, inplace=True)

    step3 = step2.merge(step1, on=["CO_UNIDADE", "DS_ATIVIDADE_PROFISSIONAL"])
    facility_staff = step3.copy()

    return facility_staff