def work_phonebook():
    choice=show_menu()
    phone_book=read_txt("phonebook.txt")
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input("Введите фамилию абонента: ")
        elif choice==3:
            tel_number=input("Введите номер телефона: ")
        elif choice==4:
            subscriber_data=[]
            fields=["Фамилия","Имя","Телефон","Описание"]
            for i in range(0,4):
                subscriber_data.append(str(input(f'{fields[i]}')))
            # subscriber_data=input('Введите через запятую: Фамилию, Имя, номер телефона,описание')
            phone_book.append(add_new_subscriber(subscriber_data, phone_book))
            print(phone_book)
        elif choice==5:
            out_file=input('Введите название файла:')
            print(copy_to_file('phonebook.txt', out_file))
        elif choice==6:
            write_txt('phonebook.txt',phone_book)
        elif choice==7:
            choice=co_out()
        choice=show_menu()

 def show_menu():
    print("\n Выберите необходимое действие:\n"
          "1. Отобразить весь справочник \n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить отчет \n"
          "6. Сохранить в БД \n"
          "7. Закончить работу\n")
    choice=int(input())
    return choice
        
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия','Имя','Телефон','Описание']
    with open (filename, 'r',encoding='ult-8') as phb:
        for line in phb:
            line=line.replace("\n""")
            record = dict(zip(fields,line.split(',')))
                    #dict (((фамилия, иванов), (имя, Точка), ...))
                    # print(record)
            phone_book.append(record)
    return phone_book
        
def find_by_subscr(phone_book, value, flag):
    if flag==0: print('Поиск по фамилии')
    else: print('Поиск по номеру')
    for i in range(len(phone_book)):

        if [m for m in phone_book[i].values()][flag]==value:
            res = '------------------\n'
            for teg1, teg2 in phone_book[i].items():

                res = f'{res} {teg1}:{teg2} \n'
            res = f'{res}--------------\n'
    if res=='':res= 'Абонент не найден \n'
    return res

def write_txt(filename, phone_book):
    with open(filename,'w', encoding='utf=8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                print(v)
                s= s+v+','
            phout.write(f'{s[:-1]}\n')

def copy_to_file(in_file, out_file):
    bd_tel=open(in_file,"r",encoding='utf-8')
    out_csv=open(out_file,"w",encoding='utf-8')

    line_count=0
    for line in bd_tel:
        if line !="\n":
            print(line)
            out_csv.write(line)
            line_count+=1
    bd_tel.close()
    out_csv.close()
    return f'Сформирован файл {out_file}'

def add_new_subscriber(subscriber_data, phone_book):
    fields=['Фамилия','Имя','Телефон','Описание']
    record= dict(zip(fields,subscriber_data))
    for ph_dic in phone_book:
        for teg1, teg2 in ph_dic.items():
            print(f'{teg1}:{teg2}')
        print("------")
    return record

 def work_phonebook()      
