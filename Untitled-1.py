import time
import os

clear = lambda: os.system('cls')

vbr = int(input("Добро пожаловать в мою новеллу \n1. Играть \n2. Выход \n"))
clear()

info = {'name': None, 'age': None, 'gender': None}

def start_game():
    print("Добро пожаловать в мою текстовую новеллу!")
    info['name'] = input("Как вас зовут? ")
    info['age'] = input("Сколько вам лет? ")
    info['gender'] = input("Какого вы пола? ")
    print("Спасибо что ввели данные о себе) \nПриятной игры!) ")
    time.sleep(2)
    clear()
    game()

def game():
         print("Однажды, в небольшом городке по имени Пайтония, \nживут два героя – Петя и Вася. \nПетя — талантливый программист \nВася — начинающий художник.")
         print()
         time.sleep(4)
         print("(Все действия будут происходить от лица Пети)")
         time.sleep(3)
         print("*Вы сидите в школьном кабинете, \nрассматривете падающий снег в утренних потёмках...")
         time.sleep(3)
         print("*К вам подходит Вася и говорит: \n--Петька, привет! Помню ты в компах разбираешься, Поможешь? ")
         time.sleep(3)
         print("Выберите ответ: \n1. Да, давай, с чем? \n2. Я не разбираюсь в компах, вы ошиблись адресом)")
         vbr = int(input("Ваш ответ: "))
         if vbr == 1:
                game2()
         elif vbr == 2:
                print("Блин-блинский, ну лааадно, удачи тебе")
                
                time.sleep(2)
                vbrk = int(input("1. Повторить попытку \n2. Выйти \nВаш ответ: "))
                if vbrk == 1:
                    clear()
                    game()        
                else:
                    exit
                    print("Игра окончена")
print()

            
        
def game2():
    print("(Петя) --Да, давай, с чем?")
    time.sleep(3)
    print(" Ну смотри, во первых мне нужно установить виндовс на свой новенький компудахтер")
    time.sleep(2)
    print("*Вы сели за парту")
    time.sleep(2)
    print("*Открыли ноут")
    time.sleep(2)
    print("Ваши действия: \n 1. Поискать флешку в кармане \n 2. Поискать флешку в рюкзаке")
    vbrk = int(input())
    if vbrk == 1:
          print("В кармане ничего не оказалось кроме карточницы и жвачки...")    
          time.sleep(3)
          clear()
          game2()
    elif vbrk == 2:
         time.sleep(2)
         clear()
         game3()
print()

def game3():
      print("Вы начали рыться в рюкзаке и спустя минуты 2 находите долгожданную флешку)))")
      time.sleep(2)
      print("Делее вставляете флешку в ноутбук и скачиваете ")
      examp = int(input("2+2="))
      if examp == 4:
            examp = int(input("2^6="))
            if examp == 64:
                  examp = int(input("64*2+7^2="))
                  if examp == 177:
                        print("Вы успешно установаили винду")
                        game4()
                  else:
                        print("Ответ не верный(((")
                        time.sleep(2)
                        vbrk = int(input("1. Повторить попытку \n2. Выйти \nВаш ответ: "))
                        if vbrk == 1:
                            clear()
                            game3()        
                        else:
                            exit
                            print("Игра окончена")
            else:
                print("Ответ не верный(((")
                time.sleep(2)
                vbrk = int(input("1. Повторить попытку \n2. Выйти \nВаш ответ: "))
                if vbrk == 1:
                    clear()
                    game3()        
                else:
                    exit
                    print("Игра окончена")
      else:
        print("Ответ не верный(((")
        time.sleep(2)
        vbrk = int(input("1. Повторить попытку \n2. Выйти \nВаш ответ: "))
        if vbrk == 1:
             clear()
             game3()        
        else:
            exit
            print("Игра окончена")
def game4():
     print("(Вася)--Урааа, а теперь можешь скачать мне приложение в котором можно рисовать?)")
     time.sleep(3)
     print("(Петя)--Слушай, может с этим ты сам справишься?")
     time.sleep(2)
     print("(Вася)--у меня не получится, ты ж программист")
     time.sleep(2)
     print("(Петя)--Да, только давай на следующей перемене это сделаю...")
     time.sleep(2)
     print("И с того момента, началась их дружба...)")
     time.sleep(2)
     print("\n         Продолжение следует")
     time.sleep(1)
     print("Понравилась игра?) Можете продолжить или выйти из игры) \n1. Играть заново \n2. Выйти ")
     vbr = int(input())
     if vbr == 1:
        clear()
        game()    
     else:
        clear()
        print('пока') and exit
print()
     
if vbr == 1:
    start_game()    
else:
    print('пока') and exit