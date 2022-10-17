from PIL import Image
import numpy as np
import os
import cv2
import numpy as np
import random
import os.path

#nome do projeto
Projeto = "Alien"
#nome das pastas
A1 = "background"
A2 = "base"
A3 = "olhos"
A4 = "boca"
A5 = "nariz"
A6 = "chapeu"
A7 = "oculos"
A8 = "resultado"
A9 = "roupa"
A10 = "acessorio"
A11 = "barba"
# Chance de gerar um nft com essas caracteristicas#
CBarba = 30
CAcessorio = 60
COculos=40
Cchapeu = 60
Croupa=95
#Quantas cores serão usadas
cores_padrão= 12
#Se o presonagem tem ou não nariz
TemNariz=0
#
OculosCobreOlho = [1]
#






def criar_pastas():
    os.mkdir('./'+ Projeto)
    os.mkdir('./'+ Projeto + '/' + A1)
    os.mkdir('./'+ Projeto + '/' + A2)
    os.mkdir('./'+ Projeto + '/' + A3)
    os.mkdir('./'+ Projeto + '/' + A4)
    os.mkdir('./'+ Projeto + '/' + A5)
    os.mkdir('./'+ Projeto + '/' + A6)
    os.mkdir('./'+ Projeto + '/' + A7)
    os.mkdir('./'+ Projeto + '/' + A8)
    os.mkdir('./'+ Projeto + '/' + A9)
    os.mkdir('./'+ Projeto + '/' + A10)
    os.mkdir('./'+ Projeto + '/' + A11)

def salvar_png():
    img = Image.new('RGBA', (2508,3541), (255, 255, 255, 0))
    img.save('./'+ Projeto + '/' + A1 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A2 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A3 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A4 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A5 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A6 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A7 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A8 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A9 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A10 + '/' "0.png", "PNG")
    img.save('./'+ Projeto + '/' + A11 + '/' "0.png", "PNG")

def menu():
    escolha = input('\nEscolha qual a opção desejada: '+  '\n1:Criar NFT ' + '\n2: Criar novas cores\n'+ '3:Criar cores randomicas\n' +  '4:Metralhadora randomica\n' + '5:Criar n NFTs randomicos\n'+ '6:Deletar um arquivo\n'+
                    '7:Gerar N cores padroes\n' + '8:Gerar 12 cores padroes de um item\n' + '9:Gerar 12 cores padroes para todos os items de uma pasta\n'+
                    '10:Gerar 12 cores padroes para todos os items de todas as pastas\n' + '11:Permutar tudo\n' + '12:Deletar uma sequencia de arquivos\n' +
                    '13:Ordenar um diretorio\n' +'14:Criar n NFTs randomicos seletiva\n' +'15:Gerar tag\n'+ '99:Encerrar o programa\n' )
    if escolha == '1':
        Criar_nft()
        menu()
    if escolha == '2':
        Pasta = escolher_pasta()
        Arquivo = escolher_arquivo()
        hue = escolher_hue() 
        Criar_novas_cores(Pasta, Arquivo, hue)
        menu()
    if escolha == '3':
        Pasta = escolher_pasta()
        Arquivo = escolher_arquivo()
        Criar_novas_cores(Pasta, Arquivo, random_colors())
        menu()
    if escolha == '4':
         print('Quantas cores você quer gerar?\n ')
         conter = int(input())
         Pasta = escolher_pasta()
         Arquivo = escolher_arquivo()
         x = 0
         while x < conter:
             x += 1
             R = random_colors()  
             Criar_novas_cores(Pasta, Arquivo, R)    
         menu()
    if escolha == '5':
        print ('Quantos arquivos você quer gerar?\n ')
        conter = int(input())
        x = 0
        while x < conter:
            Criar_nft_randomico()
            x += 1
        menu()
    if escolha == '6':
        print ('Identifique os arquivos que você quer deletar\n ')
        Pasta = escolher_pasta()
        Arquivo = escolher_arquivo()
        Deletar(Pasta, Arquivo)
        menu()

    if escolha == '7':
        print ('Identifique o arquivo que você quer gerar novas cores\n ')
        Pasta = escolher_pasta()
        Arquivo = escolher_arquivo()
        Numero = input('Escolha o numero de cores que você quer gerar: ')
        gerar_cores_padrão(Pasta, Arquivo, Numero)
        menu()
    if escolha == '8':
        print ('Identifique o arquivo que você quer gerar novas cores\n ')
        Pasta = escolher_pasta()
        Arquivo = escolher_arquivo()
        gerar_cores_padrão(Pasta, Arquivo, int(cores_padrão))
        menu()
    if escolha == '9':
        print ('Identifique a pasta que você quer gerar novas cores\n ')
        Pasta = escolher_pasta()
        automatico(Pasta)
        menu()
    if escolha == '10':
        automatico2()
        menu()
    if escolha == '11':
        automatico3()
        menu()
    if escolha == '12':
        print ('Identifique os arquivos que você quer deletar\n ')
        Pasta = escolher_pasta()
        Arquivo = escolher_arquivo()
        print ('Identifique o ultimo arquivo que você quer deletar\n ')
        Arquivo2 = escolher_arquivo()
        Delete_roll(Pasta, Arquivo, Arquivo2)
        menu()
    if escolha == '13':
        Pasta = escolher_pasta()
        ordenar(Pasta)
        menu()

    if escolha == '14':
        print ('Quantos arquivos você quer gerar?\n ')
        conter = int(input())
        x = 0
        print ('Indique os valores ou r para randomizar:\n')
        Criar_nft_seletivo(conter)
        x += 1
        menu()
    if escolha == '15':
        file = escolher_arquivo()
        print('\nInforme qual o log:\n')
        log = input()
        log
        tagmaker(file, log)
        menu()
    if escolha == '99':
        exit()
    else:
        print("Opção invalida.")
        menu()

def ordenar(pasta):
    
    contagem = 0
    percorrer =0
    total = numero_ele_p(pasta)
    while contagem < int(num_arquivos(pasta)) :
        path =('./'+ Projeto + '/' + pasta + '/' + str(percorrer) + ".png")
        percorrer+= 1
        if os.path.isfile(path):
            newfile = ('./'+ Projeto + '/' + pasta + '/' + str(contagem) + ".png")
            contagem+=1
            os.rename(path, newfile)
            


def Deletar(pasta, arquivo):
    os.remove('./'+ Projeto + '/' + pasta + '/' + str(arquivo) + ".png")
    print("Arquivo removido")
    num = num_arquivos(pasta) - 1
    indice = int(arquivo)
    while indice < int(num_arquivos(pasta)) :
        P = indice
        indice += 1
        file = ('./'+ Projeto + '/' + pasta + '/' + str(indice) + ".png")
        newfile = ('./'+ Projeto + '/' + pasta + '/' + str(P) + ".png")
        os.rename(file, newfile)
        
        
def Delete_roll(pasta, inicial, final):
    auxi= int(inicial)
    end = int(final)
    roll = end - auxi + 1
    go = 0
    while go < roll:
        Deletar(pasta, auxi)
        #auxi += 1
        go+=1

def num_arquivos(pasta):
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)   
    return(num)



def escolher_hue():
    escolha = input('\nEscolha um valor entre 0 e 180:\n')
    return (escolha)

    
def escolher_pasta():
    

    pasta = input('\nInsira 1 para ' + A1 + '\nInsira 2 para ' + A2 + '\nInsira 3 para ' + A3 + '\nInsira 4 para ' + A4 +'\nInsira 5 para ' + A5 + '\nInsira 6 para ' + A6 + '\nInsira 7 para ' + A7 + '\nInsira 8 para ' + A8 + '\n' + 'Insira 9 para ' + A9  + '\nInsira 10 para ' + A10 + '\nInsira 11 para ' + A11 +'\n' )
    if pasta == '1':
        e = A1 
    elif pasta == '2':
        e = A2
    elif pasta == '3':
        e = A3
    elif pasta == '4':
        e = A4
    elif pasta == '5':
        e = A5
    elif pasta == '6':
        e = A6
    elif pasta == '7':
        e = A7
    elif pasta == '8':
        e = A8
    elif pasta == '9':
        e = A9
    elif pasta == '10':
        e = A10
    elif pasta == '11':
        e = A11    
    else:
        print('\nOpção invalida\n')
        menu()
   
    return (e)

def escolher_arquivo():
    escolha = input('\nAgora escolha o arquivo:\n')
    return (escolha)

def chance_reduzida(Porcentagem):
    sorteio = random.randint(0, 100)    
    if sorteio <= Porcentagem:
        return 1
    else:
        return 0



    
def Criar_nft_randomico():
        
    
    pasta = A1
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    Tipe1 = random.randint(1, (num - 1))

    pasta = A2
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    Tipe2 = random.randint(1, (num - 1))

    pasta = A3
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    Tipe3 = random.randint(1, (num - 1))

    pasta = A4
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    Tipe4 = random.randint(1, (num - 1))

    pasta = A5
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    Tipe5 = random.randint(0, (num - 1))

    pasta = A6
    if chance_reduzida(Cchapeu)== 1:
        list = os.listdir('./'+ Projeto + '/' + pasta )
        num = len(list)
        Tipe6 = random.randint(0, (num - 1))
    else:
        Tipe6 = 0

    pasta = A7
    if chance_reduzida(COculos)== 1:
        list = os.listdir('./'+ Projeto + '/' + pasta )
        num = len(list)
        Tipe7 = random.randint(0, (num - 1))
    else:
        Tipe7 = 0
    
    pasta = A9
    if chance_reduzida(Croupa)== 1:
        list = os.listdir('./'+ Projeto + '/' + pasta )
        num = len(list)
        Tipe9 = random.randint(0, (num - 1))
    else:
        Tipe9 = 0

        
    pasta = A10
    if chance_reduzida(CAcessorio)== 1:
        list = os.listdir('./'+ Projeto + '/' + pasta )
        num = len(list)
        Tipe10 = random.randint(0, (num - 1))
    else:
        Tipe10 = 0    

    pasta = A11
    if chance_reduzida(CBarba)== 1:
        list = os.listdir('./'+ Projeto + '/' + pasta )
        num = len(list)
        Tipe11 = random.randint(0, (num - 1))
    else:
        Tipe11 = 0
    


    img1 = Image.open('./'+ Projeto + '/' +A1 + '/' + str(Tipe1) +".png")
    img2 = Image.open('./'+ Projeto + '/' +A2 + '/' + str(Tipe2) +".png")
    img3 = Image.open('./'+ Projeto + '/' +A3 + '/' + str(Tipe3) +".png")
    img4 = Image.open('./'+ Projeto + '/' +A4 + '/' + str(Tipe4) +".png")
    img5 = Image.open('./'+ Projeto + '/' +A5 + '/' + str(Tipe5) +".png")
    img6 = Image.open('./'+ Projeto + '/' +A6 + '/' + str(Tipe6) +".png")
    img7 = Image.open('./'+ Projeto + '/' +A7 + '/' + str(Tipe7) +".png")
    img9 = Image.open('./'+ Projeto + '/' +A9 + '/' + str(Tipe9) +".png")
    img10 = Image.open('./'+ Projeto + '/' +A10 + '/' + str(Tipe10) +".png")
    img11 = Image.open('./'+ Projeto + '/' +A11 + '/' + str(Tipe11) +".png")
    Base = Image.open('./'+ Projeto + '/' +A8 + '/' +"0.png")

    Base.paste(img1, (0, 0), img1)
    Base.paste(img2, (0, 0), img2)
    Base.paste(img9, (0, 0), img9)
    Base.paste(img3, (0, 0), img3)
    Base.paste(img4, (0, 0), img4)
    Base.paste(img5, (0, 0), img5)
    Base.paste(img7, (0, 0), img7)
    Base.paste(img9, (0, 0), img9)
    Base.paste(img11, (0, 0), img11)
    Base.paste(img10, (0, 0), img10)
    Base.paste(img6, (0, 0), img6)
    

    list = os.listdir('./'+ Projeto + '/' +A8 )
    num = len(list)
    if addLog(Tipe1, Tipe2, Tipe3, Tipe4, Tipe5, Tipe6, Tipe7, Tipe9, Tipe10, Tipe11, num) == 0:
        Base.save('./'+ Projeto + '/' +A8 + '/' + str(num) +'.png',"PNG")
    
    img1.close
    img2.close
    img3.close
    img4.close
    img5.close
    img6.close
    img7.close
    img9.close
    img10.close
    img11.close
    Base.close


def Criar_nft_automatico(Tipe1, Tipe2, Tipe3, Tipe4, Tipe5, Tipe6, Tipe7, Tipe9, Tipe10, Tipe11):
        


    img1 = Image.open('./'+ Projeto + '/' +A1 + '/' + str(Tipe1) +".png")
    img2 = Image.open('./'+ Projeto + '/' +A2 + '/' + str(Tipe2) +".png")
    img3 = Image.open('./'+ Projeto + '/' +A3 + '/' + str(Tipe3) +".png")
    img4 = Image.open('./'+ Projeto + '/' +A4 + '/' + str(Tipe4) +".png")
    img5 = Image.open('./'+ Projeto + '/' +A5 + '/' + str(Tipe5) +".png")
    img6 = Image.open('./'+ Projeto + '/' +A6 + '/' + str(Tipe6) +".png")
    img7 = Image.open('./'+ Projeto + '/' +A7 + '/' + str(Tipe7) +".png")
    img9 = Image.open('./'+ Projeto + '/' +A9 + '/' + str(Tipe9) +".png")
    img10 = Image.open('./'+ Projeto + '/' +A10 + '/' + str(Tipe10) +".png")
    img11 = Image.open('./'+ Projeto + '/' +A11 + '/' + str(Tipe11) +".png")
    Base = Image.open('./'+ Projeto + '/' +A8 + '/' +"0.png")
    
    Base.paste(img1, (0, 0), img1)
    Base.paste(img2, (0, 0), img2)
    Base.paste(img9, (0, 0), img9)
    Base.paste(img3, (0, 0), img3)
    Base.paste(img4, (0, 0), img4)
    Base.paste(img5, (0, 0), img5)
    Base.paste(img7, (0, 0), img7)
    Base.paste(img9, (0, 0), img9)    
    Base.paste(img11, (0, 0), img11)
    Base.paste(img10, (0, 0), img10)
    Base.paste(img6, (0, 0), img6)
    

    list = os.listdir('./'+ Projeto + '/' +A8 )
    num = len(list)
    if addLog(Tipe1, Tipe2, Tipe3, Tipe4, Tipe5, Tipe6, Tipe7, Tipe9, Tipe10, Tipe11, num) == 0:
        Base.save('./'+ Projeto + '/' +A8 + '/' + str(num) +'.png',"PNG")
    
    img1.close
    img2.close
    img3.close
    img4.close
    img5.close
    img6.close
    img7.close
    img9.close
    img10.close
    img11.close
    Base.close


    
def Criar_nft_seletivo(numero_de_vezes):
        
    tipe1 = input('Insira qual o ' + A1 + ': ')
    tipe2 = input('Insira qual o ' + A2 + ': ')
    tipe3 = input('Insira qual o ' + A3 + ': ')
    tipe4 = input('Insira qual o ' + A4 + ': ')
    tipe5 = input('Insira qual o ' + A5 + ': ')
    tipe6 = input('Insira qual o ' + A6 + ': ')
    tipe7 = input('Insira qual o ' + A7 + ': ')
    tipe9 = input('Insira qual o ' + A9 + ': ')
    tipe10 = input('Insira qual o ' + A10 + ': ')
    tipe11 = input('Insira qual o ' + A11 + ': ')
    x = 0
    while x < numero_de_vezes :
        x += 1
        Tipe1 = tipe1
        Tipe2 = tipe2
        Tipe3 = tipe3
        Tipe4 = tipe4
        Tipe5 = tipe5
        Tipe6 = tipe6
        Tipe7 = tipe7
        Tipe9 = tipe9
        Tipe10 = tipe10
        Tipe11 = tipe11
        if (tipe1 == 'r'):
            num = retrandom(A1)
            Tipe1 = random.randint(1, (num - 1))
        if (tipe2 == 'r'):
            num = retrandom(A2)
            Tipe2 = random.randint(1, (num - 1) )                          
        if (tipe3 == 'r'):
            num = retrandom(A3)
            Tipe3 = random.randint(1, (num - 1))
        if (tipe4 == 'r'):
            num = retrandom(A4)
            Tipe4 = random.randint(1, (num - 1))
        if (tipe5 == 'r'):
            num = retrandom(A5)
            Tipe5 = random.randint(0, (num - 1))
            
        if (tipe6 == 'r'):
            if chance_reduzida(Cchapeu)== 1:
                num = retrandom(A6)
                Tipe6 = random.randint(1, (num - 1))
            else:
                Tipe6 = 0
            
        if (tipe7 == 'r'):
            if chance_reduzida(COculos)== 1:
                num = retrandom(A7)
                Tipe7 = random.randint(1, (num - 1))
            else:
                Tipe7= 0 

        if (tipe9 == 'r'):
            if chance_reduzida(Croupa)== 1:
                num = retrandom(A9)
                Tipe9 = random.randint(1, (num - 1))
            else:
                Tipe9= 0
                
        if (tipe10 == 'r'):
            if chance_reduzida(CAcessorio)== 1:
                num = retrandom(A10)
                Tipe10 = random.randint(1, (num - 1))
            else:
                Tipe10 = 0
                
        if (tipe11 == 'r'):
            if chance_reduzida(CBarba)== 1:
                num = retrandom(A11)
                Tipe11 = random.randint(1, (num - 1))
            else:
                Tipe11 = 0


        
        img1 = Image.open('./'+ Projeto + '/' +A1 + '/' + str(Tipe1) +".png")
        img2 = Image.open('./'+ Projeto + '/' +A2 + '/' + str(Tipe2) +".png")
        img3 = Image.open('./'+ Projeto + '/' +A3 + '/' + str(Tipe3) +".png")
        img4 = Image.open('./'+ Projeto + '/' +A4 + '/' + str(Tipe4) +".png")
        img5 = Image.open('./'+ Projeto + '/' +A5 + '/' + str(Tipe5) +".png")
        img6 = Image.open('./'+ Projeto + '/' +A6 + '/' + str(Tipe6) +".png")
        img7 = Image.open('./'+ Projeto + '/' +A7 + '/' + str(Tipe7) +".png")
        img9 = Image.open('./'+ Projeto + '/' +A9 + '/' + str(Tipe9) +".png")
        img10 = Image.open('./'+ Projeto + '/' +A10 + '/' + str(Tipe10) +".png")
        img11 = Image.open('./'+ Projeto + '/' +A11 + '/' + str(Tipe11) +".png")
        Base = Image.open('./'+ Projeto + '/' +A8 + '/' +"0.png")

        Base.paste(img1, (0, 0), img1)
        Base.paste(img2, (0, 0), img2)
        Base.paste(img9, (0, 0), img9)
        Base.paste(img3, (0, 0), img3)
        Base.paste(img4, (0, 0), img4)
        Base.paste(img5, (0, 0), img5)
        Base.paste(img7, (0, 0), img7)
        Base.paste(img9, (0, 0), img9)
        Base.paste(img11, (0, 0), img11)
        Base.paste(img10, (0, 0), img10)
        Base.paste(img6, (0, 0), img6)



        list = os.listdir('./'+ Projeto + '/' +A8 )
        num = len(list)
        #print(addLog(A1, A2, A3, A4, A5, A6, A7,A9,A10, A11, num))    
        if addLog(int(Tipe1), int(Tipe2), int(Tipe3), int(Tipe4), int(Tipe5), int(Tipe6), int(Tipe7), int(Tipe9), int(Tipe10), int(Tipe11), int(num)) == 0:
            Base.save('./'+ Projeto + '/' +A8 + '/' + str(num) +'.png',"PNG")

        img1.close
        img2.close
        img3.close
        img4.close
        img5.close
        img6.close
        img7.close
        img9.close
        img10.close
        img11.close
        Base.close










def Criar_nft():
        
    Tipe1 = input('Insira qual o ' + A1 + ': ')
    Tipe2 = input('Insira qual o ' + A2 + ': ')
    Tipe3 = input('Insira qual o ' + A3 + ': ')
    Tipe4 = input('Insira qual o ' + A4 + ': ')
    Tipe5 = input('Insira qual o ' + A5 + ': ')
    Tipe6 = input('Insira qual o ' + A6 + ': ')
    Tipe7 = input('Insira qual o ' + A7 + ': ')
    Tipe9 = input('Insira qual o ' + A9 + ': ')
    Tipe10 = input('Insira qual o ' + A10 + ': ')
    Tipe11 = input('Insira qual o ' + A11 + ': ')


    img1 = Image.open('./'+ Projeto + '/' +A1 + '/' + Tipe1 +".png")
    img2 = Image.open('./'+ Projeto + '/' +A2 + '/' + Tipe2 +".png")
    img3 = Image.open('./'+ Projeto + '/' +A3 + '/' + Tipe3 +".png")
    img4 = Image.open('./'+ Projeto + '/' +A4 + '/' + Tipe4 +".png")
    img5 = Image.open('./'+ Projeto + '/' +A5 + '/' + Tipe5 +".png")
    img6 = Image.open('./'+ Projeto + '/' +A6 + '/' + Tipe6 +".png")
    img7 = Image.open('./'+ Projeto + '/' +A7 + '/' + Tipe7 +".png")
    img9 = Image.open('./'+ Projeto + '/' +A9 + '/' + Tipe9 +".png")
    img10 = Image.open('./'+ Projeto + '/' +A10 + '/' + Tipe10 +".png")
    img11 = Image.open('./'+ Projeto + '/' +A11 + '/' + Tipe11 +".png")
    Base = Image.open('./'+ Projeto + '/' +A8 + '/' +"0.png")

    Base.paste(img1, (0, 0), img1)
    Base.paste(img2, (0, 0), img2)
    Base.paste(img9, (0, 0), img9)
    Base.paste(img3, (0, 0), img3)
    Base.paste(img4, (0, 0), img4)
    Base.paste(img5, (0, 0), img5)
    Base.paste(img7, (0, 0), img7)
    Base.paste(img9, (0, 0), img9)
    Base.paste(img11, (0, 0), img11)
    Base.paste(img10, (0, 0), img10)
    Base.paste(img6, (0, 0), img6)



    list = os.listdir('./'+ Projeto + '/' +A8 )
    num = len(list)
    #print(addLog(A1, A2, A3, A4, A5, A6, A7,A9,A10, A11, num))    
    if addLog(int(Tipe1), int(Tipe2), int(Tipe3), int(Tipe4), int(Tipe5), int(Tipe6), int(Tipe7), int(Tipe9), int(Tipe10), int(Tipe11), int(num)) == 0:
        Base.save('./'+ Projeto + '/' +A8 + '/' + str(num) +'.png',"PNG")
    
    img1.close
    img2.close
    img3.close
    img4.close
    img5.close
    img6.close
    img7.close
    img9.close
    img10.close
    img11.close
    Base.close






def rgb_to_hsv(rgb):
    
    rgb = rgb.astype('float')
    hsv = np.zeros_like(rgb)
    hsv[..., 3:] = rgb[..., 3:]
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    maxc = np.max(rgb[..., :3], axis=-1)
    minc = np.min(rgb[..., :3], axis=-1)
    hsv[..., 2] = maxc
    mask = maxc != minc
    hsv[mask, 1] = (maxc - minc)[mask] / maxc[mask]
    rc = np.zeros_like(r)
    gc = np.zeros_like(g)
    bc = np.zeros_like(b)
    rc[mask] = (maxc - r)[mask] / (maxc - minc)[mask]
    gc[mask] = (maxc - g)[mask] / (maxc - minc)[mask]
    bc[mask] = (maxc - b)[mask] / (maxc - minc)[mask]
    hsv[..., 0] = np.select(
        [r == maxc, g == maxc], [bc - gc, 2.0 + rc - bc], default=4.0 + gc - rc)
    hsv[..., 0] = (hsv[..., 0] / 6.0) % 1.0
    return hsv

def hsv_to_rgb(hsv):
    
    rgb = np.empty_like(hsv)
    rgb[..., 3:] = hsv[..., 3:]
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    i = (h * 6.0).astype('uint8')
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    conditions = [s == 0.0, i == 1, i == 2, i == 3, i == 4, i == 5]
    rgb[..., 0] = np.select(conditions, [v, q, p, p, t, v], default=v)
    rgb[..., 1] = np.select(conditions, [v, v, v, q, p, p], default=t)
    rgb[..., 2] = np.select(conditions, [v, p, t, v, v, q], default=p)
    return rgb.astype('uint8')


def shift_hue(arr,hout):
    hsv=rgb_to_hsv(arr)
    hsv[...,0]=hout
    rgb=hsv_to_rgb(hsv)
    return rgb

def Criar_novas_cores(pasta, arquivo, hue):
    img = Image.open('./'+ Projeto + '/' +pasta + '/' + str(arquivo) +".png").convert('RGBA')
    arr = np.array(img)
    #New_hue = int(hue)
    New_hue = int(hue) /360.0
    #New_hue = - New_hue
    #New_hue = (180- int(hue) )/360.0
    green_hue = (180-78)/360.0
    red_hue = (180-180)/360.0

    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    
    new_img = Image.fromarray(shift_hue(arr,New_hue), 'RGBA')
    new_img.save('./'+ Projeto + '/' + pasta + '/' + str(num)+".png", "PNG")

    #new_img = Image.fromarray(shift_hue(arr,green_hue), 'RGBA')
    #new_img.save('tweeter_green.png')


def gerar_cores_padrão(pasta, arquivo, numero):
    numero= int(numero)
    PA = 360//numero
    Fator = 0
    x = 0
    while x < numero:
             
             Criar_novas_cores(pasta, arquivo, Fator)
             Fator += PA
             x += 1
             
def automatico(pasta):
    
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    contador = 1
    numero = int(cores_padrão)
    while contador < num:
        gerar_cores_padrão(pasta, contador, numero)
        contador+= 1

def automatico2():
    automatico(A1)
    automatico(A2)
    automatico(A3)
    automatico(A5)
    automatico(A6)
    automatico(A7)
    automatico(A9)
    automatico(A10)
    automatico(A11)

def automatico3():
    contador = 0
    #pasta= A1
    maximo= combinações_possiveis()// (NumA1() * NumA2() * NumA3())
    #numero_cores = cores_padrão
    #num = elementos_pasta(pasta)
    n1 = 1
    n2 = 1
    n3 = 1
    n4 = 1
    n5 = 0     
    n6 = 0
    n7 = 0
    n9 = 0
    n10 = 0
    n11 = 0
    
    while contador < maximo:
      n1 =  random.randint(1, NumA1())
      n2 =  random.randint(1, NumA2())
      n3 =  random.randint(1, NumA3())
      Criar_nft_automatico(n1, n2, n3, n4, n5, n6, n7, n9, n10, n11)
      contador += 1
      #if n1 < NumA1():
       #   n1 += 1
      #elif n2 < NumA2():
       #   n2 += 1
        #  n1=1
      #if n3 < NumA3():
       #   n3 += 1
         # n1=1
        #  n2=1
      if n4 < NumA4():
          n4 += 1
          #n1=1
          #n2=1
         # n3=1
          
      elif n6 < NumA6():
          n6 += 1
          #n1=1
          #n2=1
          #n3=1
          n4=1
      elif n7 < NumA7():
          n7 += 1
          #n1=1
          #n2=1
          #n3=1
          n4=1
          n6=1
      elif n9 < NumA9():
          n9 += 1
          #n1=1
          #n2=1
          #n3=1
          n4=1
          n6=1
          n7=1
      elif n10 < NumA10():
          n10 += 1
          #n1=1
          #n2=1
          #n3=1
          n4=1
          n6=1
          n7=1
          n9=1
      elif n11 < NumA11():
          n11 += 1
          #n1=1
          #n2=1
          #n3=1
          n4=1
          n6=1
          n7=1
          n9=1
          n10=1
      
      

            
        
        #Criar_nft_automatico(n1, n2, n3, n4, n5, n6, n7, n9, n10, n11)

def elementos_pasta(pasta):
    list = os.listdir('./'+ Projeto + '/' + pasta )
    num = len(list)
    return (num)

def combinações_possiveis():
    tot= 1
    tot = NumA1()* NumA2()* NumA3()* NumA4()* NumA6()* NumA7()* NumA9()* NumA10()* NumA11()
    if tot ==0:
        return 1
    if tot > 0:
        return tot
def numero_total():
    tot= 0
    tot = NumA1()+ NumA2()+ NumA3()+ NumA4()+ NumA5()+ NumA6()+ NumA7()+ NumA9()+ NumA10()+ NumA11()
    return tot
def numero_ele_p(Pasta):
    if (Pasta == A1):
        return NumA1()
    elif (Pasta == A2):
        return NumA2()
    elif (Pasta == A3):
        return NumA3()
    elif (Pasta == A4):
        return NumA4()
    elif (Pasta == A5):
        return NumA5()
    elif (Pasta == A6):
        return NumA6()
    elif (Pasta == A7):
        return NumA7()
    elif (Pasta == A8):
        return NumA8()
    elif (Pasta == A9):
        return NumA9()
    elif (Pasta == A10):
        return NumA10()
    elif (Pasta == A11):
        return NumA11()
    else:
        return 0
    
def NumA1():
    return (elementos_pasta(A1)- 1)
def NumA2():
    return (elementos_pasta(A2) - 1)
def NumA3():
    return (elementos_pasta(A3)- 1)
def NumA4():
    return (elementos_pasta(A4)- 1)
def NumA5():
    return (elementos_pasta(A5)- 1)
def NumA6():
    return (elementos_pasta(A6)- 1)
def NumA7():
    return (elementos_pasta(A7)- 1)
def NumA8():
    return (elementos_pasta(A8)- 1)
def NumA9():
    return (elementos_pasta(A9)- 1)
def NumA10():
    return (elementos_pasta(A10)- 1)
def NumA11():
    return (elementos_pasta(A11)- 1)
    


def addLog(A1, A2, A3, A4, A5, A6, A7,A9,A10, A11, num):
    arquivo = open('./'+ Projeto + '/'+'log.txt', 'r')
    for q in OculosCobreOlho:
        if A7 == q:
            A3 = 0
    arquivando = (str(A1) +'.'+ str(A2)+'.' + str(A3)+'.' + str(A4)+'.' + str(A5)+'.' + str(A6)+'.' + str(A7)+'.' + str(A9)+'.' + str(A10)+'.' + str(A11))
    lista = arquivo.readlines() # readlinesssssss
    Teste = 0
    arquivo.close
    for n in lista:
        if n == arquivando:
            Teste = 1
            print ('\nVocê gerou uma arquivo repetido de codigo :' + arquivando +', precione enter')
            input()
            
    if Teste == 0 :
        arquivo = open('./'+ Projeto + '/'+'log.txt', 'a')
        arquivo.write('\n'+ str(num) + ':')
        arquivo.write('\n'+str(arquivando))
        tagmaker(str(num), str(arquivando))
        arquivo.close
        return 0
    elif Teste == 1:
        return 1


def tagbackground(background):
    background_simples = [1,7,8,9,10,11,12,13,14,15,16,17,18]
    background_florestal = [2, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29,30]
    background_ondas = [3, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    background_degrade_circular = [4, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
    background_spray = [ 5, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
    background_raio = [6, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]


    
    if(background == '0'):
        return ('Background : none')
    for bg in background_simples:
        if background == str(bg):
            return ('Background : Simple')
    for bg in background_florestal:
        if background == str(bg):
            return ('Background : Forest')
    for bg in background_ondas:
        if background == str(bg):
            return ('Background : waves')
    for bg in background_degrade_circular:
        if background == str(bg):
            return ('Background :gradient')
    for bg in background_spray:
        if background == str(bg):
            return ('Background : spray')
    for bg in background_raio:
        if background == str(bg):
            return ('Background : lightning')
    return('Background : Não catalogado')
    
def tagbase(base):
    base_Yellow_Green =[1]
    base_Orangy_Yellow =[2]
    base_Pinkish_Purple =[3]
    base_Magenta_Red = [4]
    base_Orangy_Red =[5]
    base_Bluish_Cyan =[6]
    base_Red =[7]
    base_Green=[8]
    base_Green_Cyan =[9]
    base_Cyan =[10]
    base_Cyan_Blue=[11]
    base_Blue =[12]

    if(base == '0'):
        return ('Base : none')
    elif(base == '1'):
        return ('Base : Yellow_Green')
    elif(base == '2'):
        return ('Base : Orangy_Yellow')        
    elif(base == '3'):
            return ('Base : Pinkish_Purple')        
    elif(base == '4'):
        return ('Base : Magenta_Red')        
    elif(base == '5'):
        return ('Base : Bluish_Cyan')        
    elif(base == '6'):
        return ('Base : Yellow_Green')        
    elif(base == '7'):
        return ('Base : Red')        
    elif(base == '8'):
        return ('Base : Green')        
    elif(base == '9'):
        return ('Base : Green_Cyan')        
    elif(base == '10'):
        return ('Base : Cyan')
    elif(base == '11'):
        return ('Base : Cyan_Blue')
    elif(base == '12'):
        return ('Base : Blue')
    else:
        return ('Base : Não Catalogada')


def tagolho(olhos):
    olhos_looking_side=[1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    olhos_3_dot = [2, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    olhos_4_dot =[3, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    olhos_cute_1=[4, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    olhos_standart_1 =[5, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
    olhos_standart_2 =[6, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]
    olhos_standart_3 =[7, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]
    olhos_standart_4 =[8, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]
    olhos_cute_2=[9,106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]
    olhos_black1 = [118]
    olhos_black2 = [119]
    olhos_black3 = [120]
    olhos_black4 = [121]
    olhos_black5 = [122]
    olhos_black6 = [123]             
        
    if(olhos == '0'):
            return ('eyes : none')
    for ol in olhos_looking_side:
        if olhos == str(ol):
            return ('eyes : cat eyes')
    for ol in olhos_3_dot:
        if olhos == str(ol):
            return ('eyes : 3 dot')
    for ol in olhos_4_dot:
        if olhos == str(ol):
            return ('eyes : infinite')
    for ol in olhos_cute_1:
        if olhos == str(ol):
            return ('eyes : shy')
    for ol in olhos_standart_1:
        if olhos == str(ol):
            return ('eyes : lizard eyes')
    for ol in olhos_standart_2:
        if olhos == str(ol):
            return ('eyes : eyelashes')
    for ol in olhos_standart_3:
        if olhos == str(ol):
            return ('eyes : rock')
    for ol in olhos_standart_4:
        if olhos == str(ol):
            return ('eyes : alien eyes')
    for ol in olhos_cute_2:
        if olhos == str(ol):
            return ('eyes : anime eyes')
    for ol in olhos_black1:
        if olhos == str(ol):
            return ('eyes : uwu eyes')
    for ol in olhos_black2:
        if olhos == str(ol):
            return ('eyes : confuse')
    for ol in olhos_black3:
        if olhos == str(ol):
            return ('eyes : sleeping')
    for ol in olhos_black4:
        if olhos == str(ol):
            return ('eyes : dead')
    for ol in olhos_black5:
        if olhos == str(ol):
            return ('eyes : happy')
    for ol in olhos_black6:
        if olhos == str(ol):
            return ('eyes : myopic')
        
    return('eyes : Não catalogado')

def tagboca(boca):
    boca_cigarro = [1]
    boca_gato = [2]
    boca_palhaço = [3]
    boca_3 = [4]
    boca_smiley_1 =[5, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    boca_sad = [6, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    boca_o = [7, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    boca_smiley_2 =[8, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
    boca_smiley_3 = [9]
    boca_sad_2 = [10]
    boca_black1 = [11]
    boca_dot = [12]
    boca_moe = [13]
    boca_P = [14]
    boca_sad3 = [15]
    boca_dot2 = [16]
    boca_s =[17]
    if(boca == '0'):
            return ('mouth : none')
    for bo in boca_cigarro:
        if boca == str(bo):
            return ('mouth : cigarette')
    for bo in boca_gato:
        if boca == str(bo):
            return ('mouth : cat')
    for bo in boca_palhaço:
        if boca == str(bo):
            return ('mouth : clown')
    for bo in boca_3:
        if boca == str(bo):
            return ('mouth : kiss')
    for bo in boca_smiley_1:
        if boca == str(bo):
            return ('mouth : drooling')
    for bo in boca_sad:
        if boca == str(bo):
            return ('mouth : shocked')
    for bo in boca_o:
        if boca == str(bo):
            return ('mouth : whistling')
    for bo in boca_smiley_2:
        if boca == str(bo):
            return ('mouth : happy')
    for bo in boca_smiley_3:
        if boca == str(bo):
            return ('mouth : cheerful')
    for bo in boca_sad_2:
        if boca == str(bo):
            return ('mouth : sad')
    for bo in boca_black1:
        if boca == str(bo):
            return ('mouth : smile')
    for bo in boca_3:
        if boca == str(bo):
            return ('mouth : clown mouth')
    for bo in boca_dot:
        if boca == str(bo):
            return ('mouth : loathing')
    for bo in boca_moe:
        if boca == str(bo):
            return ('mouth : uwu')
    for bo in boca_P:
        if boca == str(bo):
            return ('mouth : mocking')
    for bo in boca_sad3:
        if boca == str(bo):
            return ('mouth : sad')
    for bo in boca_dot2:
        if boca == str(bo):
            return ('mouth : thinking')
    for bo in boca_s:
        if boca == str(bo):
            return ('mouth : shy')
    return('mouth : Não catalogado')




def tagchapeu(chapeu):
    chapeu_headphone =[1, 2, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
    chapeu_coroa =[3, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86 ]
    chapeu_Pony_tail = [4, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
    chapeu_laço = [5, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    chapeu_atleta=[6 , 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    chapeu_astronauta = [7, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]
    chapeu_viking = [8, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]
    chapeu_cabelinho =[9, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]
    chapeu_punk =[10, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]
    chapeu_guirlanda=[11, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182]
    chapeu_reggae= [12, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194]
    chapeu_hippie = [13, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206]
    chapeu_palhaço = [14, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
    chapeu_estrela =[15, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]
    chapeu_slime = [16, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242]
    chapeu_cozinheiro = [17, 18, 19]
    chapeu_talinho = [20, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254]
    chapeu_bob = [21, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266]
    chapeu_jud=[22, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278]
    chapeu_social_faixa1 = [23, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290]
    chapeu_social_faixa2= [24, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302]
    chapeu_social_faixa3= [25, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314]
    chapeu_gorro=[26, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326]
    chapeu_social_faixa5=[27, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338]
    chapeu_preto_faixa=[28, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350]
    chapeu_detetive= [29, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362]
    chapeu_social_faixa_preta=[30, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374]
    chapeu_boina =[31, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386]
    chapeu_pescador = [32, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398]
    chapeu_bone =[33, 34, 35, 36, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446]
    chapeu_cabelinho_trump = [37, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458]
    chapeu_jojo=[38]
    chapeu_gorro_2=[39, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470]
    chapeu_guirlanda_2=[40, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482]
    chapeu_florzinha= [41, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494]
    chapeu_sorvete=[42, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506]
    chapeu_papel_higienico=[43]
    chapeu_genie=[44, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518]
    chapeu_hamburguer =[45, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530]
    chapeu_boina_2 = [46, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542]
    chapeu_arrow=[47, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554]
    chapeu_chifre_1 =[48, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566]
    chapeu_chifre_2 =[49]
    chapeu_chifre_3 =[50, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578]
    
    if(chapeu == '0'):
            return ('Hat : none')
    for ch in chapeu_headphone:
        if chapeu == str(ch):
            return ('Hat : headphone')

    for ch in chapeu_coroa:
        if chapeu == str(ch):
            return ('Hat : crown')
    for ch in chapeu_Pony_tail:
        if chapeu == str(ch):
            return ('Hat : Ponytail')
    for ch in chapeu_laço:
        if chapeu == str(ch):
            return ('Hat : tie')
    for ch in chapeu_atleta:
        if chapeu == str(ch):
            return ('Hat : sports')
    for ch in chapeu_astronauta:
        if chapeu == str(ch):
            return ('Hat : astronaut')
    for ch in chapeu_viking:
        if chapeu == str(ch):
            return ('Hat : viking')
    for ch in chapeu_cabelinho:
        if chapeu == str(ch):
            return ('Hat : wig')
    for ch in chapeu_punk:
        if chapeu == str(ch):
            return ('Hat : punk')
    for ch in chapeu_guirlanda:
        if chapeu == str(ch):
            return ('Hat : wreath')
    for ch in chapeu_reggae:
        if chapeu == str(ch):
            return ('Hat : reggae')
    for ch in chapeu_hippie:
        if chapeu == str(ch):
            return ('Hat : hippie')
    for ch in chapeu_palhaço:
        if chapeu == str(ch):
            return ('Hat : clown')
    for ch in chapeu_estrela:
        if chapeu == str(ch):
            return ('Hat : star')
    for ch in chapeu_slime:
        if chapeu == str(ch):
            return ('Hat : slime')
    for ch in chapeu_cozinheiro:
        if chapeu == str(ch):
            return ('Hat : Chef')
    for ch in chapeu_talinho:
        if chapeu == str(ch):
            return ('Hat : plant')
    for ch in chapeu_bob:
        if chapeu == str(ch):
            return ('Hat : jamaican')
    for ch in chapeu_jud:
        if chapeu == str(ch):
            return ('Hat : pilbox')
    for ch in chapeu_social_faixa1:
        if chapeu == str(ch):
            return ('Hat : boater')
    for ch in chapeu_social_faixa2:
        if chapeu == str(ch):
            return ('Hat : top hat')
    for ch in chapeu_social_faixa3:
        if chapeu == str(ch):
            return ('Hat : cowboy')
    for ch in chapeu_gorro:
        if chapeu == str(ch):
            return ('Hat : chullo')
    for ch in chapeu_social_faixa5:
        if chapeu == str(ch):
            return ('Hat : porkpie')
    for ch in chapeu_preto_faixa:
        if chapeu == str(ch):
            return ('Hat : top hat')
    for ch in chapeu_detetive:
        if chapeu == str(ch):
            return ('Hat : deerstalker')
    for ch in chapeu_social_faixa_preta:
        if chapeu == str(ch):
            return ('Hat : hamburg')
    for ch in chapeu_boina:
        if chapeu == str(ch):
            return ('Hat : ascot cap')
    for ch in chapeu_pescador:
        if chapeu == str(ch):
            return ('Hat : bucket hat')
    for ch in chapeu_bone:
        if chapeu == str(ch):
            return ('Hat : cap')
    for ch in chapeu_cabelinho_trump:
        if chapeu == str(ch):
            return ('Hat : hair')
    for ch in chapeu_jojo:
        if chapeu == str(ch):
            return ('Hat : peaked hat')
    for ch in chapeu_gorro_2:
        if chapeu == str(ch):
            return ('Hat : beanie')
    for ch in chapeu_guirlanda_2:
        if chapeu == str(ch):
            return ('Hat : wreath')
    for ch in chapeu_florzinha:
        if chapeu == str(ch):
            return ('Hat : flower')
    for ch in chapeu_sorvete:
        if chapeu == str(ch):
            return ('Hat : icecream')
    for ch in chapeu_papel_higienico:
        if chapeu == str(ch):
            return ('Hat : toilet paper')
    for ch in chapeu_genie:
        if chapeu == str(ch):
            return ('Hat : fez')
    for ch in chapeu_hamburguer:
        if chapeu == str(ch):
            return ('Hat : hamburguer')
    for ch in chapeu_boina_2:
        if chapeu == str(ch):
            return ('Hat : beret')
    for ch in chapeu_arrow:
        if chapeu == str(ch):
            return ('Hat : arrow')
    for ch in chapeu_chifre_1:
        if chapeu == str(ch):
            return ('Hat : reindeer horn')
    for ch in chapeu_chifre_2:
        if chapeu == str(ch):
            return ('Hat : rhino horn')
    for ch in chapeu_chifre_3:
        if chapeu == str(ch):
            return ('Hat : unicorn horn')
    return('Hat : Não catalogado')



def tagoculos(oculos):
    oculos_RV=[1]
    oculos_3d =[2]
    oculos_alien=[3, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    oculos_tv=[4, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
    oculos_TL =[5]
    oculos_circular=[6, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
    oculos_listras=[7, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    oculos_quadrado=[8, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
    oculos_zedroguinha=[9, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
    oculos_quadrado_2=[10]
    oculos_neve=[11, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]
    oculos_circular_2=[12, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
    oculos_circular_3=[13]
    oculos_circular_4=[14]
    oculos_circular_5=[15]
    oculos_circular_6=[16]
    oculos_circular_7=[17]
    oculos_v=[18, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]
    oculos_dbz=[19, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]
    oculos_monoculos=[20]
    oculos_coração=[21, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]
    oculos_quadrado_3=[22]
    oculos_carnaval=[23, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167]

    if(oculos == '0'):
        return ('Glasses : none')
    for oc in oculos_RV:
        if oculos == str(oc):
            return ('Glasses : RV')
    for oc in oculos_3d:
        if oculos == str(oc):
            return ('Glasses : 3d')
    for oc in oculos_alien:
        if oculos == str(oc):
            return ('Glasses : Alien glasses')
    for oc in oculos_tv:
        if oculos == str(oc):
            return ('Glasses : TV glasses')
    for oc in oculos_TL:
        if oculos == str(oc):
            return ('Glasses : meme glasses')
    for oc in oculos_circular:
        if oculos == str(oc):
            return ('Glasses : pilot')
    for oc in oculos_listras:
        if oculos == str(oc):
            return ('Glasses : striped sunglasses')
    for oc in oculos_quadrado:
        if oculos == str(oc):
            return ('Glasses : square')
    for oc in oculos_zedroguinha:
        if oculos == str(oc):
            return ('Glasses : mirrored')
    for oc in oculos_quadrado_2:
        if oculos == str(oc):
            return ('Glasses : wrap')
    for oc in oculos_neve:
        if oculos == str(oc):
            return ('Glasses : googles')
    for oc in oculos_circular_2:
        if oculos == str(oc):
            return ('Glasses : aviator')
    for oc in  oculos_circular_3:
        if oculos == str(oc):
            return ('Glasses : basic')
    for oc in  oculos_circular_4:
        if oculos == str(oc):
            return ('Glasses : cat eye')
    for oc in  oculos_circular_5:
        if oculos == str(oc):
            return ('Glasses : round eye')
    for oc in  oculos_circular_6:
        if oculos == str(oc):
            return ('Glasses : normal')
    for oc in  oculos_circular_7:
        if oculos == str(oc):
            return ('Glasses : sunglasses')
    for oc in  oculos_v:
        if oculos == str(oc):
            return ('Glasses : cool glasses')
    for oc in  oculos_dbz:
        if oculos == str(oc):
            return ('Glasses : cyberpunk')
    for oc in  oculos_monoculos:
        if oculos == str(oc):
            return ('Glasses : monocle')
    for oc in  oculos_coração:
        if oculos == str(oc):
            return ('Glasses : heart')
    for oc in  oculos_quadrado_3:
        if oculos == str(oc):
            return ('Glasses : nerd')
    for oc in  oculos_carnaval:
        if oculos == str(oc):
            return ('Glasses : mask')


    
    
    return('Glasses : Não catalogado')

def tagroupa(roupa):


    roupa_V =[1, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
    roupa_sem_manga=[2, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    roupa_sem_manga_2=[3, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
    roupa_maio=[4,63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
    roupa_capuz=[5, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
    roupa_suspensorio=[6, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
    roupa_camiseta_padrão=[7, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    roupa_terno=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]
    roupa_camiseta_padrão_2=[20, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]
    roupa_gola_alta=[21, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]
    roupa_grega=[22, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]
    roupa_gola_alta_v= [23, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182]
    roupa_capuz_2=[24, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194]
    roupa_mini_V=[25, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206]
    roupa_aberta=[26, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
    roupa_florida=[219, 220,223,224]
    roupa_cozinheiro=[221]
    roupa_cocos=[222]
    if(roupa == '0'):
        return ('Clothes : none')
    for ro in roupa_V:
        if roupa == str(ro):
            return ('Clothes : V shirt')
    for ro in roupa_sem_manga:
        if roupa == str(ro):
            return ('Clothes : no sleeves')
    for ro in roupa_sem_manga_2:
        if roupa == str(ro):
            return ('Clothes : no sleeves')
    for ro in  roupa_maio:
        if roupa == str(ro):
            return ('Clothes : swimsuit')
    for ro in roupa_capuz:
        if roupa == str(ro):
            return ('Clothes : hoody')
    for ro in roupa_suspensorio:
        if roupa == str(ro):
            return ('Clothes : suspender')
    for ro in roupa_camiseta_padrão:
        if roupa == str(ro):
            return ('Clothes : T-shirt')
    for ro in roupa_terno:
        if roupa == str(ro):
            return ('Clothes : suit')
    for ro in roupa_camiseta_padrão_2:
        if roupa == str(ro):
            return ('Clothes : T-shirt')
    for ro in roupa_gola_alta:
        if roupa == str(ro):
            return ('Clothes : turtleneck')
    for ro in roupa_grega:
        if roupa == str(ro):
            return ('Clothes : geek')
    for ro in roupa_gola_alta_v:
        if roupa == str(ro):
            return ('Clothes : turtleneck')
    for ro in roupa_capuz_2:
        if roupa == str(ro):
            return ('Clothes : hoody')
    for ro in roupa_mini_V:
        if roupa == str(ro):
            return ('Clothes : T-shirt')
    for ro in roupa_aberta:
        if roupa == str(ro):
            return ('Clothes : Alien style')
    for ro in roupa_florida:
        if roupa == str(ro):
            return ('Clothes : hawaii clothes')
    for ro in roupa_cozinheiro:
        if roupa == str(ro):
            return ("Clothes : cook's clothes")
    for ro in roupa_cocos:
        if roupa == str(ro):
            return ("Clothes : coconut bikini")


    return('Clothes : Não catalogado')
def tagacessorio(acessorio):
    
    acessorio_colar=[1,2,3,8]
    acessorio_coleira=[4,5,6, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
    acessorio_mascara=[7, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]
    acessorio_nariz_palhaço=[9, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    acessorio_chifre=[10, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
    acessorio_corrente=[11, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]
    acessorio_gravata_aberta=[12]
    acessorio_gravata_semi_solta= [13, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    acessorio_frozinha=[14, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
    acessorio_band_aid=[15, 112, 113, 114, 115, 116]
    
    if(acessorio == '0'):
        return ('Accessory : none')
    for ac in acessorio_colar:
        if acessorio == str(ac):
            return ('Accessory : necklace')
    for ac in acessorio_coleira:
        if acessorio == str(ac):
            return ('Accessory : choker')
    for ac in acessorio_mascara:
        if acessorio == str(ac):
            return ('Accessory : mask')
    for ac in acessorio_nariz_palhaço:
        if acessorio == str(ac):
            return ('Accessory : clown nose')
    for ac in acessorio_chifre:
        if acessorio == str(ac):
            return ('Accessory : horn')
    for ac in acessorio_corrente:
        if acessorio == str(ac):
            return ('Accessory : chain')
    for ac in acessorio_gravata_aberta:
        if acessorio == str(ac):
            return ('Accessory : loose tie')
    for ac in acessorio_gravata_semi_solta:
        if acessorio == str(ac):
            return ('Accessory : loose tie')
    for ac in acessorio_frozinha:
        if acessorio == str(ac):
            return ('Accessory : piercing')
    for ac in acessorio_band_aid:
        if acessorio == str(ac):
            return ('Accessory : bandaid')






    
    return('Accessory : Não catalogado')




def tagbarba(barba):
    barba_chevron=[5,25,26]
    barba_imperial=[4,13,17,18,24,29,33,39]
    barba_english=[3,9,10,11,12,21,27]
    barba_fu_manchu=[2,35]
    barba_pencil=[1,6]
    barba_painter=[7,8,15,28]
    barba_horseshoe=[30,31,32]
    barba_pyramidal=[22,37]
    barba_walrus=[14,23,34,36]
    barba_française=[16,19]
    barba_handlebear=[20]
    barba_toothbrush=[38]
    if(barba == '0'):
        return ('Beard : none')
    for be in barba_chevron:
        if barba == str(be):
            return ('Beard : chevron')
    for be in barba_imperial:
        if barba == str(be):
            return ('Beard : imperial')
    for be in barba_english:
        if barba == str(be):
            return ('Beard : english')
    for be in barba_fu_manchu:
        if barba == str(be):
            return ('Beard : fu manchu')
    for be in barba_pencil:
        if barba == str(be):
            return ('Beard : pencil')
    for be in barba_painter:
        if barba == str(be):
            return ('Beard : painter')
    for be in barba_horseshoe:
        if barba == str(be):
            return ('Beard : horseshoe')
    for be in barba_pyramidal:
        if barba == str(be):
            return ('Beard : pyramidal')
    for be in barba_walrus:
        if barba == str(be):
            return ('Beard : walrus')
    for be in barba_française:
        if barba == str(be):
            return ('Beard : française')
    for be in barba_handlebear:
        if barba == str(be):
            return ('Beard : handlebear')
    for be in barba_toothbrush:
        if barba == str(be):
            return ('Beard : toothbrush')





    
    return('Beard : Não catalogado')

    
def tagmaker(file, log):
    background, base, olhos, boca, nariz, chapeu, oculos, roupa, acessorio, barba = log.split('.')
    try:
        file =('./'+ Projeto + '/' +'tags' + '/' + file +".txt")
        arquivo = open(file, 'r+')
    except FileNotFoundError:
        arquivo = open(file, 'w+')
        arquivo.writelines(tagbackground(background))
        arquivo.writelines('\n'+tagbase(base))
        arquivo.writelines('\n'+tagolho(olhos))
        arquivo.writelines('\n'+tagboca(boca))
        arquivo.writelines('\n'+tagchapeu(chapeu))
        arquivo.writelines('\n'+tagoculos(oculos))
        arquivo.writelines('\n'+tagroupa(roupa))
        arquivo.writelines('\n'+tagacessorio(acessorio))
        arquivo.writelines('\n'+tagbarba(barba))
        arquivo.close()

        







    
    arquivo.close()
    



def random_colors():
    hue = random.randint(0, 3600)
    return(hue)


    
try:
    criar_pastas()
    salvar_png()
    print('O diretorio ' + Projeto + ' acabou de ser criado,\nfeche esse programa e o abra novamente para ir ao menu!\n Made by Bell&Leona')
    input()
    
except FileExistsError:
    menu()
