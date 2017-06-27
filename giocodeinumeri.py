import random
import time
def menu():
        print "benvenuto al GIOCO DEI NUMERI!"
        time.sleep(1)
        print "cosa vuoi fare?"
        print "1. comincia gioco"
        print "2. informazioni sul gioco"
        print "3. esci"
        risposta1 = raw_input()
        if risposta1 == "1":
                print ciao()
        if risposta1 == "2":
                print "gioco creato da Rossano Fragale"
                print menu()
                
        if risposta1 == "3":
                print 
def risposta():
        print "vuoi riprovare? (si/no)"
        risposta = raw_input()
        if risposta == "si":
                print ciao()
        elif risposta == "no":
                print "ciao!"
        exit()
        
def ciao():
        n = random.randrange(1, 100)
        m = random.randrange(1, 100)
        n_str = str(n)
        m_str = str(m)
        print "__________________GIOCATORE UMANO_____________"
        print "------------------------" + n_str + "---------------------"
        print ".                                             ."
        print ".                                             ."
        print ".                                             ."
        if n_str < 20:
                print "__________________BASSO!______________________";
        elif n_str > 80:
                print "____________________ALTO!_______________________"
        else:
                print "__________________MEZZANO!____________________"

        time.sleep(1)


        print "___________________COMPUTER___________________"
        print "------------------------" + m_str + "---------------------"
        print ".                                             ."
        print ".                                             ."
        print ".                                             ."
        if m_str == n_str:
                print "__________________UGUALI, YEA!________________"
        elif m_str > n_str:
                print "_______________TI HO BATTUTO!_________________"
        elif m_str < n_str:
                print "______________MI HAI BATTUTO, SIGH!___________"
        

        
        print risposta()
menu()

