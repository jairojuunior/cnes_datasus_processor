import pandas as pd
import numpy as np
from facility_general_characteristics import *
from facility_equipments import * 
from facility_infrastructure import * 
from facility_services import * 
from facility_staff import * 
from download_file import *
from uncompress_file import *
from file_operations import *

def standart_cnes_importer(file):
    imported = pd.read_csv(file, sep=";", header=0)
    return imported

if __name__ == "__main__":
    
    daterefs = [201903, 201904, 201905, 201906, 201907, 201908, 201909, 201910, 201911, 201912,
                202001, 202002, 202003]

    for date in daterefs:
        dateref = str(date)

        #Download zip
        download_zip("ftp://ftp.datasus.gov.br/cnes", "BASE_DE_DADOS_CNES_"+dateref+".ZIP")

        #Uncompress file
        path = uncompress_file("BASE_DE_DADOS_CNES_"+dateref+".ZIP")+"/"

        #IMPORT FILES AS DATAFRAMES

        #files on facility general characteristics
        tbEstabelecimento = standart_cnes_importer(path+"tbEstabelecimento"+dateref+".csv") #OK
        tbTipoEstabelecimento = standart_cnes_importer(path+"tbTipoEstabelecimento"+dateref+".csv") #OK
        tbMunicipio = standart_cnes_importer(path+"tbMunicipio"+dateref+".csv") #OK
        tbClientela= standart_cnes_importer(path+"tbFluxoDadosClientela"+dateref+".csv") #OK
        tbNaturezaJuridica = standart_cnes_importer(path+"tbNaturezaJuridica"+dateref+".csv") #OK
        tbTurnoAtend = standart_cnes_importer(path+"tbTurnoAtendimento"+dateref+".csv") #OK
        tbAtividade = standart_cnes_importer(path+"tbAtividade"+dateref+".csv") #OK

        #files on facility 'brick' infrastructure
        rlEstabInstFisiAssist = standart_cnes_importer(path+"rlEstabInstFisiAssist"+dateref+".csv") #OK
        tbInstalFisicaParaAssist = standart_cnes_importer(path+"tbInstalFisicaParaAssist"+dateref+".csv") #OK

        #files on facility infrastructure
        rlEstabEquipamento = standart_cnes_importer(path+"rlEstabEquipamento"+dateref+".csv") #OK
        tbEquipamento = standart_cnes_importer(path+"tbEquipamento"+dateref+".csv") #OK
        tbTipoEquipamento = standart_cnes_importer(path+"tbTipoEquipamento"+dateref+".csv") #OK


        #files on services provided
        rlEstabAtendPrestConv = standart_cnes_importer(path+"rlEstabAtendPrestConv"+dateref+".csv") #OK
        tbAtendimentoPrestado = standart_cnes_importer(path+"tbAtendimentoPrestado"+dateref+".csv") #OK
        tbConvenio = standart_cnes_importer(path+"tbConvenio"+dateref+".csv") #OK

        #files on staff
        tbCargaHorariaSus = standart_cnes_importer(path+"tbCargaHorariaSus"+dateref+".csv") #OK 
        tbAtividadeProfissional = standart_cnes_importer(path+"tbAtividadeProfissional"+dateref+".csv") #OK 

        #DATAPREP

        facility_general = get_facility_general(tbEstabelecimento, tbClientela, tbNaturezaJuridica, 
                                                tbTurnoAtend, tbAtividade, tbTipoEstabelecimento, tbMunicipio)

        facility_equipments = get_facility_equipments(rlEstabEquipamento, tbEquipamento, tbTipoEquipamento)

        facility_infrastructure = get_facility_infrastructure(rlEstabInstFisiAssist, tbInstalFisicaParaAssist)

        facility_services = get_facility_services(rlEstabAtendPrestConv, tbAtendimentoPrestado, tbConvenio)

        facility_staff = get_facility_staff(tbCargaHorariaSus, tbAtividadeProfissional)

        #OUTPUT RESULT
        create_folder(dateref+"_output")

        facility_general.to_csv(dateref+"_output/facility_general.csv")
        facility_equipments.to_csv(dateref+"_output/facility_equipments.csv")
        facility_infrastructure.to_csv(dateref+"_output/facility_infrastructure.csv")
        facility_services.to_csv(dateref+"_output/facility_services.csv")
        facility_staff.to_csv(dateref+"_output/facility_staff.csv")

        #DELETE UNCOMPRESSED FILES
        del_folder(path)
        del_file("BASE_DE_DADOS_CNES_"+dateref+".ZIP")