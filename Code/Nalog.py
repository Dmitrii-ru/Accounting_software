from tkinter import filedialog as fd


def nal():
    """Рабочая версия2"""
    with open(fd.askopenfilename(), encoding='utf-8') as file, open(fd.askopenfilename(), encoding='utf-8') as file2, open(fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("CSV files", "*.csv"),
                       ("All files", "*.*"))), "w+") as file1:
        f, vse_po_0_fnew, vse_NE_po_0_fnew = [i.strip().replace(u'\xa0', '').replace(",", ".").split("!") for i in
                                              file.readlines()[9::]], [], []
        # Больничный
        f1 = [i.strip().replace(u'\xa0', '').replace(",", ".").split("!") for i in file2.readlines()[1::]]

        # Общий список сотрудников
        list_name_in_f = set()
        # Кого обработали
        list_name_in_fnew = set()
        # Больничные
        list_sick = []
        for i in f:
            list_name_in_f.add(i[0])
            i[15] = float(0)
        # Добавил БЛ
        for i in f:
            for j in f1:
                if i[0] == j[2] and j[3] != '':
                    i[15] += float(j[3])

        for j in f:
            if j[2] != '' and j[9] != '' and j[10] != '' and float(j[2]) > 13890:
                q1 = round(float(j[2]) - 13890, 2) if j[-1] == '' else round((float(j[2]) - float(j[-1])) - 13890, 2)
                q2 = round(float(q1 * 10 / 100) + 3055.8, 2)
                q3 = round(q2 - float(j[6]), 2)
                q4 = round((q1 * 5 / 100) + 708.39)
                q5 = round(q4 - float(j[11]))
                q8 = round(float(j[2]) * 0.5 / 100, 2) if j[-1] == '' else round(
                    (float(j[2]) - float(j[-1])) * 0.5 / 100, 2)
                q9 = round(q8 - float(j[10]))
                if int(q5) == 0 and int(q3) == 0 and int(q9) == 0:
                    vse_po_0_fnew.append(
                        [j[0], f"Минуc  Мрот = {q1}", f"ПФ 10% = {q2}", f"ФФОМС = {q4}", f"ФСС травм = {q8} ",
                         f"Разница ПФ = {int(q3)}",
                         f"Разница ФФОМС = {int(q5)}", f"Разница ФСС травм = {int(q9)} "])
                else:
                    vse_NE_po_0_fnew.append(
                        [j[0], f"Минуc  Мрот = {q1}", f"ПФ 10% = {q2}", f"ФФОМС = {q4}", f"ФСС травм = {q8} ",
                         f"Разница ПФ = {int(q3)}",
                         f"Разница ФФОМС = {int(q5)}", f"Разница ФСС травм = {int(q9)} "])

                list_name_in_fnew.add(j[0])
                if j[-1] != 0.0:
                    list_sick.append([j[0], j[-1]])

            if j[2] != '' and j[9] != '' and j[10] != '' and float(j[2]) < 13890:
                w1 = round(float(j[2]), 2) if j[-1] == '' else round(float(j[2]) - float(j[-1]), 2)
                w2 = round(w1 * 22 / 100, 2)
                w3 = round(w2 - float(j[6]), 2)
                w4 = round(((w1 * 5.10) / 100), 2)
                w5 = round(w4 - float(j[11]), 2)
                w6 = round(w1 * 2.9 / 100, 2)
                w7 = round(w6 - float(j[9]), 2)
                w8 = round(w1 * 0.5 / 100, 2)
                w9 = round(w8 - float(j[10]))
                if int(q5) == 0 and int(q3) == 0 and int(q9) == 0:
                    vse_po_0_fnew.append(
                        [j[0], f"Минуc  Мрот = {q1}", f"ПФ 10% = {q2}", f"ФФОМС = {q4}", f"ФСС травм = {q8} ",
                         f"Разница ПФ = {int(q3)}",
                         f"Разница ФФОМС = {int(q5)}", f"Разница ФСС травм = {int(q9)} "])
                else:
                    vse_NE_po_0_fnew.append(
                        [j[0], f"Минуc  Мрот = {q1}", f"ПФ 10% = {q2}", f"ФФОМС = {q4}", f"ФСС травм = {q8} ",
                         f"Разница ПФ = {int(q3)}",
                         f"Разница ФФОМС = {int(q5)}", f"Разница ФСС травм = {int(q9)} "])
                list_name_in_fnew.add(j[0])
                if j[-1] != 0.0:
                    list_sick.append([j[0], j[-1]])

        print("Статистика:", file=file1)
        print("_" * len("Статистика:"), file=file1)
        print("Кол сотрудников:", len(list_name_in_f), file=file1)
        print("_" * len("Кол сотрудников:"), file=file1)
        print("Не обработано:", *(list_name_in_f - list_name_in_fnew), sep="\n", file=file1)
        print("_" * len("Больничный:"), file=file1)
        print("Больничный:", file=file1)
        for i in list_sick:
            print(*i, sep=": ", file=file1)
        print("_" * len("Разница не 0 "), file=file1)
        print(f"Разница не 0 : {len(vse_NE_po_0_fnew)} чел.", file=file1)
        for i in vse_NE_po_0_fnew:
            print("_" * len(i[0]), file=file1)
            print(*i, sep="\n", file=file1)
        print("_" * len("Разница 0"), file=file1)
        print(f"Разница 0: {len(vse_po_0_fnew)} чел.", file=file1)
        for i in vse_po_0_fnew:
            print("_" * len(i[0]), file=file1)
            print(*i, sep="\n", file=file1)


def result():
    """Рабочая версия"""
    with open(fd.askopenfilename(), encoding='utf-8') as file, open(fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("CSV files", "*.csv"),
                       ("All files", "*.*"))), "w+") as file1:

        keys = file.readline().strip().split('!')
        LIST, raiselist, a, newlist = [dict(zip(keys, line.strip().split('!'))) for line in file], [], {}, []
        keys1 = dict.fromkeys(set([LIST[x]["Сотрудник"] for x in range(len(LIST))]))
        raiselist.append(f"Статистика:")
        raiselist.append(f"Кол сотрудников: {len(keys1)}")
        raiselist.append(f"Статистика:")
        for i in sorted(keys1):
            for j in range(len(LIST)):
                if i == LIST[j]["Сотрудник"]:
                    a.setdefault(i, []).append(LIST[j])

                if "Доплата за совмещение должностей, исполнение обязанностей" in LIST[j]["Начисление"]:
                    if LIST[j]["Сотрудник"] not in raiselist:
                        raiselist[2] = "Доплата за совмещение должностей, исполнение обязанностей:"
                        raiselist.append(LIST[j]["Сотрудник"])
        for i in a:
            if len(a[i]) == 1 and a[i][0]["Оплачено часов"] != '':
                q = round((float(a[i][0]["Значение1"].replace(",", ".").replace(u'\xa0', '')) / float(
                    a[i][0]["Норма чс."].replace(",", "."))), 5)
                q1 = round(q * float(a[i][0]["Оплачено часов"].replace(",", ".").replace(u'\xa0', '')), 2)
                q2 = float(a[i][0]["Результат"].replace(",", ".").replace(u'\xa0', '')) - q1
                newlist.append([a[i][0]["Сотрудник"], f"Значение1 / Норма чс. = {q}",
                                f"Значение1 / Норма чс. * Оплачено часов = {q1}", f"Результат = {q2}"])

            if len(a[i]) == 2:
                a[i].sort(key=lambda x: x["Начисление"])
                w = round((float(a[i][1]["Значение1"].replace(",", ".").replace(u'\xa0', '')) / float(
                    a[i][1]["Норма чс."].replace(",", "."))), 5)
                w1 = round(w * float(a[i][1]["Оплачено часов"].replace(",", ".").replace(u'\xa0', '')), 2)
                w2 = float(a[i][1]["Результат"].replace(",", ".").replace(u'\xa0', '')) - w1
                w3 = round((((w * round(float(a[i][0]["Оплачено часов"].replace(",", ".").replace(u'\xa0', '')),
                                        2)) * 20) / 100), 2)
                w4 = w - float(a[i][0]["Значение2"].replace(",", "."))
                w5 = w3 - float(a[i][0]["Результат"].replace(",", ".").replace(u'\xa0', ''))
                newlist.append([a[i][1]["Сотрудник"], f"Значение1 / Норма чс. = {w}",
                                f"Значение1 / Норма чс. * Оплачено часов = {w1}", f"Результат оплачено = {w2}",
                                f"Результат нормы {w4}",
                                f"Оплачено ночных {w3}", f"Результат ночных {w5}"])
            if len(a[i]) > 2:
                raiselist.append(f"""Больше 2 строк {[a[i][1]["Сотрудник"]]}""")

        for j in raiselist:
            print(j, sep="\n", file=file1)
        for i in sorted(newlist):
            print("_" * len(i[0]), file=file1)
            print(*i, sep="\n", file=file1)
