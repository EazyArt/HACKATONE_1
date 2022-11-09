import re
import  requests





def main():
    #Отправляем get запрос
    url =  str(input('Введите ссылку:'))
    r=requests.get(url)
    # Копируем html страничку в txt
    with open("index.txt", "w", encoding='utf-8') as file:
        file.write(r.text)
    #Ищем местоимения и подсчитываем их
    Ya = re.findall(r' [Яя] ',  r.text)
    My = re.findall(r' [Мм]ы ', r.text)
    first_face_result = len(Ya)+len(My)

    Ty = re.findall(r' [Тт]ы ', r.text)
    Vy = re.findall(r' [Вв]ы ', r.text)
    On = re.findall(r' [Оо]н ', r.text)
    Ona = re.findall(r' [Оо]на ', r.text)
    Ono = re.findall(r' [Оо]но ', r.text)
    Ony = re.findall(r' [Оо]ни ', r.text)
    another_face_result = len(Ty) + len(Vy) + len(On) + len(Ona) + len(Ono) + len(Ony)

    # Выдаем результат
    if first_face_result > another_face_result:
        print("Местоимений 1-го лица, чем количество остальных личных местоимений.", "Результат:", first_face_result)
    elif  first_face_result == another_face_result:
        print("Царит равноправие")
    else:
        print("К сожалению, местоимений 1-го лица мало.","Результат местоимений не 1-го лица:", another_face_result )


if __name__ =="__main__":
    main()