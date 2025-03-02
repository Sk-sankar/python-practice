class Enemy:
    def __init__(self,type,health=10,attack=1):
        self.type=type
        self.health=health
        self.attack=attack
        
    def get_the_type(self):
        return self.type
        
    def talk(self):
        print(f"I am a {self.type} enemy")
        
    def walk(self):
        print(f"{self.type}is  walking forward")