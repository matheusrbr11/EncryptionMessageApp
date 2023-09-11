from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(False,False)
root.title("Encryption Message App")

Label(root,text="ENCODE DECODE",font='arial 20 bold').pack()
Label(root,text="© Matheusrbr11",font='arial 9 bold').pack(side=BOTTOM)

text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'encode'):
        result.set(Encode(private_key.get(), text.get()))
    elif(mode.get() == 'decode'):
        result.set(Decode(private_key.get(), text.get()))
    else:
        result.set('Invalid Mode')


def Reset():
    text.set("")
    private_key.set("")
    mode.set("")
    result.set("")

Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MODE(encode or decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = result, bg ='ghost white').place(x=290, y = 150)

Label(root, font = 'arial 12 bold', text ='RESULT').place(x=60, y = 150)
Button(root, font = 'arial 10 bold', text = 'RESET'  ,padx =2,bg ='LightGray' ,command = Reset).place(x=180, y = 220)
Button(root, font = 'arial 10 bold' ,text = 'RESULT' ,width =6, command = Mode,bg = 'LimeGreen', padx=2).place(x=260, y = 220)

root.mainloop()