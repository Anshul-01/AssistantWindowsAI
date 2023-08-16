def myself(Name, monthYear, Founder1):
    sentence = f"My name is {Name} and I'm an Voice-Based Vitual Assistant for Windows and was invented in {monthYear} by {Founder1}. Also I was based on Python language."
    return sentence
    
def gameRulesInstruction():
    return f"Today we are Playing game whose name is : STONE PAPER and SCISSOR. For that few rules are there also as Mentioned on Screen. Rule is you have to choose any one of three: Either you have to choose Stone or Paper or Scissor. Higher prefernce gonna win this game. Let's Begin."

if __name__ == "__main__":
    me = input("Enter AI name:\t")
    monthYear = input("When it was established:\t")
    name1 = input("Enter the first founder name:\t")
    name2 = input("Enter the second founder name:\t")
    Myself = myself(me, monthYear, name1, name2)
    print(Myself)
