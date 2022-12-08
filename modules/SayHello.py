class SayHello :
  def __init__(self,target= "world"):
    self.target = target
  def say(self):
    print("Hello, " + self.target + "!")

  

if __name__ == "__main__" :
  app = SayHello()
  app.say()
  app = SayHello("Someone")
  app.say()
    
