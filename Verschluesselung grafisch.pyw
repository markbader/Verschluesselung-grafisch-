v='Verschlüsselung'
bg='#f5f5f5'
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo
import winsound
import random
root=tk.Tk()
root.state('zoomed')
root.title('VERSCHLÜSSELUNG')
root.wm_iconbitmap('../Verschlüsselung/data/verschlüsselung.ico')
root.resizable(width='no', height='no')
root.config(bg=bg)
höhe=root.winfo_screenheight()
breite=root.winfo_screenwidth()
#Startvorgang
start=tk.Label(root, text='', bg=bg, font=('DigifaceWide', 30))
start_unten=tk.Label(root, text='\u00a9 by Mark Bader 2013', bg=bg, justify='center', font=('Arial', 10), fg='grey')
start.place(x=breite/100*20, y=höhe/100*40, width=breite/100*60)
start_unten.place(x=breite/100*45, y=höhe/100*90)
z=0
while(z<len(v)):
    z=z+1
    root.after(150, start.configure(text=v[0:z]))
    root.after(0, winsound.PlaySound('../Verschlüsselung/data/taste.wav', winsound.SND_FILENAME))
    root.update()
root.after(2000, None)
start.destroy()
start_unten.place_forget()
root.resizable(width='yes', height='yes')
min_width=int(root.winfo_screenwidth()/100*50)
min_height=int(root.winfo_screenheight()/100*42)
root.minsize(min_width, min_height)
#Hauptprogramm beginnt
def datei_öffnen_funktion(event):
    global fehler
    datei_suchen=tk.filedialog.askopenfilename(filetypes=[('Text-Dateien', '*.txt'), ('Alle Dateien', '*.*'), ('HTML-Datein', '*.html'), ('Python-Datei', ('*.py', '*.pyw'))])
    try:
        datei_lesen=open(datei_suchen, 'r')
        datei_gelesen=datei_lesen.read()
        text.delete('1.0', 'end')
        text.insert('1.0', datei_gelesen)
        datei_lesen.close()
    except:
        fehler=fehler+1
def datei_speichern_funktion(event):
    global fehler
    ordner_suchen=tk.filedialog.asksaveasfilename(title='Speichern', initialfile='Unbenannt.txt', filetypes=[('Text-Dateien', '*.txt'), ('HTML-Datein', '*.html'), ('Python-Datei', ('*.py', '*.pyw'))])
    try:
        zeichenanzahl=len(ordner_suchen)
        endung_prüfen=str(ordner_suchen[zeichenanzahl-4]+ordner_suchen[zeichenanzahl-3]+ordner_suchen[zeichenanzahl-2]+ordner_suchen[zeichenanzahl-1])
        if endung_prüfen=='.txt':
            datei_schreiben=open(ordner_suchen, 'w')
            datei_geschrieben=datei_schreiben.write(str(text.get('1.0', 'end')))
            datei_schreiben.close()
        else:
            ordner_suchen=str(ordner_suchen + '.txt')
            datei_schreiben=open(ordner_suchen, 'w')
            datei_geschrieben=datei_schreiben.write(str(text.get('1.0', 'end')))
            datei_schreiben.close()
    except:
        fehler=fehler+1
def text_verschlüsseln_funktion(event):
    global code
    global verschlüsselter_text
    password2=str(eingabefeld.get())
    verschlüsselter_text=''
    passwordlänge=len(password2)
    try:
        if password2=='':
            a=tk.messagebox.showinfo('Fehler', 'Sie müssen ein Password eingeben um den Text zu verschlüsseln.')
        elif passwordlänge<5:
            a=tk.messagebox.showinfo('Fehler', 'Das Password ist zu kurz!')
        else:
            x=0
            passcode='3g!a5jn+4?äh.9mü@271q€yö}ßwhv98f76e/RN)tr7)=$s4589og9987R&§$&FUHIKT%&E/()(&guoguz§$%"§(=LNHTD%$SFW$gb7633256(&%§DFHG&/$JHKJL'
            password=''
            while(passwordlänge>x):
                zahl=random.randint(0, 840)
                normale_zahl1=code.index(password2[x])
                normale_zahl2=code.index(passcode[x%124])
                verschlüsselte_zahl1=normale_zahl1 + zahl
                verschlüsselte_zahl2=normale_zahl2 + zahl
                verschlüsselte_zahl1=str(verschlüsselte_zahl1).zfill(3)
                verschlüsselte_zahl2=str(verschlüsselte_zahl2).zfill(3)
                verschlüsselte_zahl=str(verschlüsselte_zahl1 + verschlüsselte_zahl2)
                password=password+verschlüsselte_zahl
                x=x+1
            verschlüsselter_text=''
            text_zum_verschlüsseln=str(str(password) + str(text.get('1.0', 'end')))
            Buchstabenanzahl=len(text_zum_verschlüsseln)
            x=0
            while(Buchstabenanzahl>x):
                zahl=random.randint(0, 840)
                normale_zahl1=code.index(text_zum_verschlüsseln[x])
                normale_zahl2=code.index(password2[x%passwordlänge])
                verschlüsselte_zahl1=normale_zahl1 + zahl
                verschlüsselte_zahl2=normale_zahl2 + zahl
                verschlüsselte_zahl1=str(verschlüsselte_zahl1).zfill(3)
                verschlüsselte_zahl2=str(verschlüsselte_zahl2).zfill(3)
                verschlüsselte_zahl=str(verschlüsselte_zahl1 + verschlüsselte_zahl2)
                x=x+1
                if (x%20==0) and (x!=0):
                    verschlüsselte_zahl=verschlüsselte_zahl+'\n'
                verschlüsselter_text=verschlüsselter_text+verschlüsselte_zahl
            x=0
            verschlüsselter_text=str(verschlüsselter_text)
            verschlüsselter_text=verschlüsselter_text.replace('0', '\u2501')
            verschlüsselter_text=verschlüsselter_text.replace('1', '\u2503')
            verschlüsselter_text=verschlüsselter_text.replace('2', '\u250f')
            verschlüsselter_text=verschlüsselter_text.replace('3', '\u2513')
            verschlüsselter_text=verschlüsselter_text.replace('4', '\u2517')
            verschlüsselter_text=verschlüsselter_text.replace('5', '\u251b')
            verschlüsselter_text=verschlüsselter_text.replace('6', '\u2523')
            verschlüsselter_text=verschlüsselter_text.replace('7', '\u252b')
            verschlüsselter_text=verschlüsselter_text.replace('8', '\u2533')
            verschlüsselter_text=verschlüsselter_text.replace('9', '\u253b')
            text.configure(state='normal')
            text.delete('1.0', 'end')
            text.insert('1.0', verschlüsselter_text)
    except:    
        a=tk.messagebox.showinfo('Fehler', 'Der Text enthällt Sonderzeichen die das Programm nicht deuten kann. Die Verschlüsselung ist nicht möglich.')
    text.configure(state='normal')
    datei_öffnen.configure(state='normal')
    datei_speichern.configure(state='normal')
    text_verschlüsseln.configure(state='normal')
    text_entschlüsseln.configure(state='normal')
    text.bind('<Control-s>', datei_speichern_funktion)
    text.bind('<Control-o>', datei_öffnen_funktion)
    abstand=höhe/100*38
    datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
    datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
    strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
    text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
    text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
    while(abstand>0):
        abstand=abstand-5
        datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
        datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
        text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
        text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
        strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
        text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40-abstand, width=breite/100*10-30, height=höhe/100*3)
        eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40-abstand, width=breite/100*15-30, height=höhe/100*3)
        ok_button2.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        ok_button.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50-abstand, width=breite/100*17, height=höhe/100*3)
        root.update()
    text_im_bedienfeld.place_forget()
    eingabefeld.place_forget()
    ok_button.place_forget()
    ok_button2.place_forget()
    abbrechen_button.place_forget()
    eingabefeld.delete(0, 'end')
    text.focus_set()
def text_verschlüsseln_dialog(event):
    text.configure(state='disabled')
    datei_öffnen.configure(state='disabled')
    datei_speichern.configure(state='disabled')
    text_verschlüsseln.configure(state='disabled')
    text_entschlüsseln.configure(state='disabled')
    text_im_bedienfeld.configure(text='Passwort:')
    text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40, width=breite/100*10-30, height=höhe/100*3)
    eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40, width=breite/100*15-30, height=höhe/100*3)
    ok_button.place(x=breite/100*75+25, y=höhe/100*50, width=breite/100*8-30, height=höhe/100*3)
    ok_button.bind('<Button-1>', text_verschlüsseln_funktion)
    eingabefeld.bind('<Return>', text_verschlüsseln_funktion)
    abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50, width=breite/100*17, height=höhe/100*3)
    eingabefeld.focus_set()
    eingabefeld.bind('<Escape>', abbrechen)
    abstand=0
    root.update()
    root.after(200, None)
    while(abstand<höhe/100*38):
        abstand=abstand+5
        datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
        datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
        text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
        text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
        strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
        text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40-abstand, width=breite/100*10-30, height=höhe/100*3)
        eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40-abstand, width=breite/100*15-30, height=höhe/100*3)
        ok_button.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50-abstand, width=breite/100*17, height=höhe/100*3)
        root.update()
    datei_öffnen.place_forget()
    datei_speichern.place_forget()
    strich.place_forget()
    text_verschlüsseln.place_forget()
    text_entschlüsseln.place_forget()
def text_entschlüsseln_funktion(event):
    global code
    text_zum_entschlüsseln=str(text.get('1.0', 'end'))
    text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\n', '')
    password2=str(eingabefeld.get())
    passwordlänge=len(password2)
    passcode='3g!a5jn+4?äh.9mü@271q€yö}ßwhv98f76e/RN)tr7)=$s4589og9987R&§$&FUHIKT%&E/()(&guoguz§$%"§(=LNHTD%$SFW$gb7633256(&%§DFHG&/$JHKJL'
    Buchstabenanzahl=len(text_zum_entschlüsseln)
    if password2=='':
        a=tk.messagebox.showinfo('Fehler', 'Sie müssen ein Passwort eingeben um die Datei zu entschlüsseln.')
    else:
        try:
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u2501', '0')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u2503', '1')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u250f', '2')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u2513', '3')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u2517', '4')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u251b', '5')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u2523', '6')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u252b', '7')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u2533', '8')
            text_zum_entschlüsseln=text_zum_entschlüsseln.replace('\u253b', '9')
            d=0
            e=1
            f=2
            g=3
            h=4
            i=5
            x=0
            entschlüsselter_text=''
            while(Buchstabenanzahl>i):
                ziffer2=int(text_zum_entschlüsseln[d]+text_zum_entschlüsseln[e]+text_zum_entschlüsseln[f])
                ziffer1=int(text_zum_entschlüsseln[g]+text_zum_entschlüsseln[h]+text_zum_entschlüsseln[i])
                passwordbuchstabe=code.index(password2[x%passwordlänge])
                zufallszahl=ziffer1-passwordbuchstabe
                entschlüsselter_buchstabe=ziffer2-zufallszahl
                entschlüsselter_buchstabe=code[entschlüsselter_buchstabe]
                entschlüsselter_text=entschlüsselter_text+entschlüsselter_buchstabe
                d=d+6
                e=e+6
                f=f+6
                g=g+6
                h=h+6
                i=i+6
                x=x+1
            d=0
            e=1
            f=2
            g=3
            h=4
            i=5
            x=0
            password_zum_entschlüsseln=entschlüsselter_text
            entschlüsseltes_password=''
            while(passwordlänge*6>i):
                ziffer2=int(password_zum_entschlüsseln[d]+password_zum_entschlüsseln[e]+password_zum_entschlüsseln[f])
                ziffer1=int(password_zum_entschlüsseln[g]+password_zum_entschlüsseln[h]+password_zum_entschlüsseln[i])
                passwordbuchstabe=code.index(passcode[x%124])
                zufallszahl=ziffer1-passwordbuchstabe
                entschlüsselter_buchstabe=ziffer2-zufallszahl
                entschlüsselter_buchstabe=code[entschlüsselter_buchstabe]
                entschlüsseltes_password=entschlüsseltes_password+entschlüsselter_buchstabe
                d=d+6
                e=e+6
                f=f+6
                g=g+6
                h=h+6
                i=i+6
                x=x+1
            if entschlüsseltes_password==password2:
                entschlüsselter_text=entschlüsselter_text[passwordlänge*6:-1]
                text.configure(state='normal')
                text.delete('1.0', 'end')
                text.insert('1.0', entschlüsselter_text)
            else:
                entschlüsselter_text=''
                a=tk.messagebox.showinfo('Fehler', 'Das von ihnen eingegebene Kennwort ist Falsch.')
        except:
            a=tk.messagebox.showinfo('Fehler', 'Das von ihnen eingegebene Kennwort ist Falsch.')
    text.configure(state='normal')
    datei_öffnen.configure(state='normal')
    datei_speichern.configure(state='normal')
    text_verschlüsseln.configure(state='normal')
    text_entschlüsseln.configure(state='normal')
    text.bind('<Control-s>', datei_speichern_funktion)
    text.bind('<Control-o>', datei_öffnen_funktion)
    abstand=höhe/100*38
    datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
    datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
    strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
    text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
    text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
    while(abstand>0):
        abstand=abstand-5
        datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
        datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
        text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
        text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
        strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
        text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40-abstand, width=breite/100*10-30, height=höhe/100*3)
        eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40-abstand, width=breite/100*15-30, height=höhe/100*3)
        ok_button2.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        ok_button.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50-abstand, width=breite/100*17, height=höhe/100*3)
        root.update()
    text_im_bedienfeld.place_forget()
    eingabefeld.place_forget()
    ok_button.place_forget()
    ok_button2.place_forget()
    abbrechen_button.place_forget()
    eingabefeld.delete(0, 'end')
    text.focus_set()
def text_entschlüsseln_dialog(event):
    text.configure(state='disabled')
    datei_öffnen.configure(state='disabled')
    datei_speichern.configure(state='disabled')
    text_verschlüsseln.configure(state='disabled')
    text_entschlüsseln.configure(state='disabled')
    text_im_bedienfeld.configure(text='Passwort:')
    abstand=0
    text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40-abstand, width=breite/100*10-30, height=höhe/100*3)
    eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40-abstand, width=breite/100*15-30, height=höhe/100*3)
    ok_button2.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
    ok_button2.bind('<Button-1>', text_entschlüsseln_funktion)
    eingabefeld.bind('<Return>', text_entschlüsseln_funktion)
    abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50-abstand, width=breite/100*17, height=höhe/100*3)
    eingabefeld.focus_set()
    text.bind('<Control-s>', None)
    text.bind('<Control-o>', None)
    eingabefeld.bind('<Escape>', abbrechen)
    root.update()
    root.after(200, None)
    while(abstand<höhe/100*38):
        abstand=abstand+5
        datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
        datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
        text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
        text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
        strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
        text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40-abstand, width=breite/100*10-30, height=höhe/100*3)
        eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40-abstand, width=breite/100*15-30, height=höhe/100*3)
        ok_button2.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50-abstand, width=breite/100*17, height=höhe/100*3)
        root.update()
    datei_öffnen.place_forget()
    datei_speichern.place_forget()
    strich.place_forget()
    text_verschlüsseln.place_forget()
    text_entschlüsseln.place_forget()
def abbrechen(event):
    text.configure(state='normal')
    datei_öffnen.configure(state='normal')
    datei_speichern.configure(state='normal')
    text_verschlüsseln.configure(state='normal')
    text_entschlüsseln.configure(state='normal')
    text.focus_set()
    abstand=höhe/100*38
    datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
    datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
    strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
    text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
    text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
    while(abstand>0):
        abstand=abstand-5
        datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2-abstand, width=breite/100*25-30)
        datei_speichern.place(x=breite/100*75+25, y=höhe/100*7-abstand, width=breite/100*25-30)
        text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19-abstand, width=breite/100*25-30)
        text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24-abstand, width=breite/100*25-30)
        strich.place(x=breite/100*75+25, y=höhe/100*15-abstand, width=breite/100*25-30, height=3)
        text_im_bedienfeld.place(x=breite/100*75+25, y=höhe/100*40-abstand, width=breite/100*10-30, height=höhe/100*3)
        eingabefeld.place(x=(breite/100*75+25)+(breite/100*10-30), y=höhe/100*40-abstand, width=breite/100*15-30, height=höhe/100*3)
        ok_button2.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        ok_button.place(x=breite/100*75+25, y=höhe/100*50-abstand, width=breite/100*8-30, height=höhe/100*3)
        abbrechen_button.place(x=(breite/100*75)+(breite/100*8), y=höhe/100*50-abstand, width=breite/100*17, height=höhe/100*3)
        root.update()
    text_im_bedienfeld.place_forget()
    eingabefeld.place_forget()
    ok_button.place_forget()
    ok_button2.place_forget()
    abbrechen_button.place_forget()
    eingabefeld.delete(0, 'end')
def Fenstergröße_anpassen():
    global höhe
    global breite
    j=0
    höhe2=0
    breite2=0
    while(j<1):
        höhe=root.winfo_height()
        breite=root.winfo_width()
        if (höhe!=höhe2) or (breite!=breite2):
            text.place(x=5, y=5, width=breite/100*75, height=höhe-15)
            datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2, width=breite/100*25-30)
            datei_speichern.place(x=breite/100*75+25, y=höhe/100*7, width=breite/100*25-30)
            text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19, width=breite/100*25-30)
            text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24, width=breite/100*25-30)
            strich.place(x=breite/100*75+25, y=höhe/100*15, width=breite/100*25-30, height=3)
            start_unten.place(x=breite/100*75+25, y=höhe/100*95, width=breite/100*25-30)
            scr.place(x=breite/100*75+5, y=5, width=15, height=höhe-15)
            text_im_bedienfeld.place_forget()
            eingabefeld.place_forget()
            ok_button.place_forget()
            ok_button2.place_forget()
            abbrechen_button.place_forget()
            eingabefeld.delete(0, 'end')
        höhe2=höhe
        breite2=breite
        root.update()
root.after(0, Fenstergröße_anpassen)
root.state('normal')
root.state('zoomed')
#Textfeld
text=tk.Text(root, relief='groove')
text.place(x=5, y=5, width=breite/100*75, height=höhe-60)
text.focus_set()
#Bedienfeld
datei_öffnen=tk.Label(root, bg=bg, text='Datei Öffnen', font=('DigifaceWide', 12), relief='flat')
datei_öffnen.place(x=breite/100*75+25, y=höhe/100*2, width=breite/100*25-30)
datei_speichern=tk.Label(root, bg=bg, text='Datei Speichern', font=('DigifaceWide', 12), relief='flat')
datei_speichern.place(x=breite/100*75+25, y=höhe/100*7, width=breite/100*25-30)
strich=tk.Label(root, bg='grey')
strich.place(x=breite/100*75+25, y=höhe/100*15, width=breite/100*25-30, height=3)
text_verschlüsseln=tk.Label(root, bg=bg, text='Verschlüsseln', font=('DigifaceWide', 12), relief='flat')
text_verschlüsseln.place(x=breite/100*75+25, y=höhe/100*19, width=breite/100*25-30)
text_entschlüsseln=tk.Label(root, bg=bg, text='Entschlüsseln', font=('DigifaceWide', 12), relief='flat')
text_entschlüsseln.place(x=breite/100*75+25, y=höhe/100*24, width=breite/100*25-30)
start_unten.place(x=breite/100*75+25, y=höhe/100*95, width=breite/100*25-30)
scr=tk.Scrollbar(root, command=text.yview, relief='groove')
text.config(yscrollcommand=scr.set)
scr.place(x=breite/100*75+5, y=5, width=15, height=höhe-60)
text_im_bedienfeld=tk.Label(root, bg=bg, text='')
eingabefeld=tk.Entry(root, bg=bg, show='\u26AB', relief='groove')
ok_button=tk.Label(root, bg=bg, relief='groove', text='OK')
ok_button2=tk.Label(root, bg=bg, relief='groove', text='OK')
abbrechen_button=tk.Label(root, bg=bg, relief='groove', text='ABBRECHEN')
abbrechen_button.bind('<Button-1>', abbrechen)
text.bind('<Control-s>', datei_speichern_funktion)
text.bind('<Control-o>', datei_öffnen_funktion)
datei_speichern.bind('<Button-1>', datei_speichern_funktion)
datei_öffnen.bind('<Button-1>', datei_öffnen_funktion)
text_verschlüsseln.bind('<Button-1>', text_verschlüsseln_dialog)
text_entschlüsseln.bind('<Button-1>', text_entschlüsseln_dialog)
fehler=0
code='1q\u0178ay2w\u00FFsx3e`d\u2501\u2503\u250f\u2513\u2517\u251b\u2523\u252b\u2533\u253bñc4râ\u00C6fv5tgb6zhn7u\u00E7jm8i\u00F8k,9ol.0p\u00D8ö-ßüä´+#^°!QAY"WS\u00E6X§E\\DC$RF\u00C7ÂVBGT%&ZH_NM\u00CBJU/(IK  ;:L\u00EBO)=PÖ-ÄÜ?´*' + "'" + 'èéàáýúÙÀ\u00EFÁÚÝ\níìîÛÌÍÎ\u00CFÉ\u0153€ÈûêÊóòô\u0152ÒÓÔ|@~{[]}<> '
root.mainloop()
