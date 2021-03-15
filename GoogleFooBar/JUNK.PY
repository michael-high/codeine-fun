def greeting():
    print("Hi, how are you")
def Conversation(sentence):
    
    if sentence.__contains__("hello")==True:
        greeting()
    
    
    
    
    keepgoing=input("""
    do you want continue? [y] [n]
    """)
    if keepgoing.lower()=="y":
        start=input('Ask me another question\n')
        Conversation(start)
        











def begin():
    print("""
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $     $  $ $$$ $   $   $$$$    $
    $     $  $ $   $   $   $  $    $
    $     $$$$ $$$ $   $   $  $    $
    $     $  $ $   $   $   $  $    $
    $     $  $ $$$ $$$ $$$ $$$$    $
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)
    #name jizz jazz
    
    start=input("""
    I am a chatbot for Wabash Trivia!
    Ask me something about Wabash!
    """)
    Conversation(start)
begin()



