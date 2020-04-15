
def get_facility_general(tbEstabelecimento, tbClientela, tbNaturezaJuridica, tbTurnoAtend, tbAtividade, tbTipoEstabelecimento, tbMunicipio):

    cols_step_0 = ["CO_UNIDADE", "TP_PFPJ", "NO_FANTASIA", "CO_CLIENTELA", "CO_NATUREZA_JUR",
                "CO_TIPO_ESTABELECIMENTO", "CO_TURNO_ATENDIMENTO", "TP_ESTAB_SEMPRE_ABERTO",
                "CO_ATIVIDADE_PRINCIPAL", "ST_CONEXAO_INTERNET", "CO_MUNICIPIO_GESTOR", 
                "NU_LATITUDE", "NU_LONGITUDE"]
    #Drop deactivated facilities
    step0 = tbEstabelecimento[tbEstabelecimento["CO_MOTIVO_DESAB"].isna()][cols_step_0].copy() 
    #Type of care provided
    step1 = step0.merge(tbClientela, on=["CO_CLIENTELA"], validate="many_to_one")
    #Legal nature
    step2 = step1.merge(tbNaturezaJuridica, on=["CO_NATUREZA_JUR"], validate="many_to_one")
    step2['TP_PFPJ'] = step2['TP_PFPJ'].replace({1: "PF", 3: "PJ"})
    #Service shifts
    step3 = step2.merge(tbTurnoAtend, on=["CO_TURNO_ATENDIMENTO"], validate="many_to_one")
    #Main activity
    step4 = step3.merge(tbAtividade, left_on=["CO_ATIVIDADE_PRINCIPAL"], right_on=["CO_ATIVIDADE"], 
                        validate="many_to_one")
    #Type of facility
    step5 = step4.merge(tbTipoEstabelecimento, on=["CO_TIPO_ESTABELECIMENTO"], validate="many_to_one")

    #City and state
    cols_step_6 = ['CO_UNIDADE', 'NO_FANTASIA', 'DS_TIPO_ESTABELECIMENTO', 'TP_PFPJ', 'DS_CLIENTELA',
                'DS_NATUREZA_JUR', 'TP_ESTAB_SEMPRE_ABERTO','DS_TURNO_ATENDIMENTO','DS_ATIVIDADE',
                'ST_CONEXAO_INTERNET', 'NO_MUNICIPIO', 'CO_SIGLA_ESTADO', 
                'NU_LATITUDE', 'NU_LONGITUDE']
    step6 = step5.merge(tbMunicipio, left_on=["CO_MUNICIPIO_GESTOR"], right_on=["CO_MUNICIPIO"], 
                        validate="many_to_one")[cols_step_6]
    facility_general = step6.copy()
    
    return facility_general