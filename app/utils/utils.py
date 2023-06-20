from datetime import datetime, timedelta


def remove_critical_data(data: dict, remove_data: list = None):
    for remove_key in remove_data:
        if remove_key in data.keys():
            del data[remove_key]

    if data.get("_key"):
        data["key"] = data.pop("_key")

    if data.get("_id"):
        data["id"] = data.pop("_id")

    return data


def contar_registros_por_mes(datas):
    meses_do_ano = {
        "Janeiro": 0,
        "Fevereiro": 0,
        "Março": 0,
        "Abril": 0,
        "Maio": 0,
        "Junho": 0,
        "Julho": 0,
        "Agosto": 0,
        "Setembro": 0,
        "Outubro": 0,
        "Novembro": 0,
        "Dezembro": 0,
    }

    meses_em_portugues = {
        "January": "Janeiro",
        "February": "Fevereiro",
        "March": "Março",
        "April": "Abril",
        "May": "Maio",
        "June": "Junho",
        "July": "Julho",
        "August": "Agosto",
        "September": "Setembro",
        "October": "Outubro",
        "November": "Novembro",
        "December": "Dezembro",
    }

    for data in datas:
        data_obj = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        mes = data_obj.strftime("%B")
        mes_em_portugues = meses_em_portugues.get(mes)

        if mes_em_portugues:
            meses_do_ano[mes_em_portugues] += 1

    return meses_do_ano


def datas_anteriores(data):
    data_atual = datetime.now()
    data_parametro = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

    datas_anteriores = []
    dia = data_atual.date()

    while dia > data_parametro.date():
        datas_anteriores.append(dia.strftime("%Y-%m-%d"))
        dia -= timedelta(days=1)

    return datas_anteriores


def ordenar_datas(lista_datas):
    datas_convertidas = [
        datetime.strptime(data, "%Y-%m-%d").date() for data in lista_datas
    ]
    datas_ordenadas = sorted(datas_convertidas)
    datas_formatadas = [data.strftime("%d/%m/%Y") for data in datas_ordenadas]
    return datas_formatadas
