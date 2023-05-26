import poe_chatgpt

with open('poe_cred.txt','r') as f:
    cred = f.readlines()
client = poe_chatgpt.Client(cred[0])


def ask(message):    
    for chunk in client.send_message("chinchilla", message):
        pass

    return chunk["text"]


if __name__ == "__main__":
    #Auth
    bot = 'chinchilla'
    print("The selected bot is : ", bot)
    #---------------------------------------------------------------------------

    print("Context is now cleared")
    while True:
        message = input("Human : ")
        reply = ask(message)        
        print(f"{bot} : {reply}")