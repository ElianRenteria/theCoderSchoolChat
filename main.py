import socket
import threading
import tkinter
from tkinter import scrolledtext


HOST = "192.168.1.70"
#68.7.149.165
PORT = 8000


def recieve_message(chat):
    while True:
        data = server.recv(1024)
        print(data.decode())
        chat.config(state="normal")
        chat.insert(tkinter.END,str(data.decode("utf-8"))+"\n")
        chat.config(state="disabled")

def send_message(message, inputbox):
    if message == "quit":
        recieve_thread.join()
        server.close()
        quit()
    else:
        server.send((username+": " + message).encode())
        inputbox.delete(0, 'end')



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
print("connected to server!")
username = input("Enter a username: ")




window = tkinter.Tk()
window.title("the Coder School Chat")
window.geometry("500x600")
window.resizable(False, False)

chat = scrolledtext.ScrolledText(window, width = 53, height = 33, font=("helvetica", 12), state="disabled")
chat.place(x=0, y=0)
inputBox = tkinter.Entry(window, width=50)
inputBox.place(x=0, y=570)
submit_button = tkinter.Button(window, text="submit", width=5, command=lambda:send_message(inputBox.get(), inputBox))
submit_button.place(x=420, y=565)

recieve_thread = threading.Thread(target=recieve_message, args=(chat,))
recieve_thread.start()

window.mainloop()
