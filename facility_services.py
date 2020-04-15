def get_facility_services(rlEstabAtendPrestConv, tbAtendimentoPrestado, tbConvenio):
    step0 = rlEstabAtendPrestConv.merge(tbAtendimentoPrestado, on=["CO_ATENDIMENTO_PRESTADO"],
                                        validate="many_to_one")

    cols_step_1 = ["CO_UNIDADE", "DS_ATENDIMENTO_PRESTADO", "DS_CONVENIO"]
    step1 = step0.merge(tbConvenio, on=["CO_CONVENIO"], 
                        validate="many_to_one")[cols_step_1]

    #Append all payment methods in a single line
    step2 = step1.sort_values(["CO_UNIDADE", "DS_ATENDIMENTO_PRESTADO", "DS_CONVENIO"], ascending=False)
    step2['CONVENIOS'] = step2.groupby(["CO_UNIDADE","DS_ATENDIMENTO_PRESTADO"]
                                    )["DS_CONVENIO"].transform(lambda x: ','.join(x))
    step2.drop(['DS_CONVENIO'], axis=1, inplace=True)
    step2.drop_duplicates(inplace=True, ignore_index=True)

    facility_services = step2.copy()

    return facility_services