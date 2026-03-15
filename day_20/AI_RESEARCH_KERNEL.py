class BaseAi:
    def __init__(self, name):
        self.name = name
        self.__api_key = "SECRET-8821-X" 

    def boot_up(self):
        print(f"--- {self.name} System Online. Security Key Verified. ---")

class ComputerVision(BaseAi):
    def execute_task(self): 
        print(f"[{self.name}] Analyzing pixel density... Object Detected.")

class NaturalLanguage(BaseAi):
    def execute_task(self):
        print(f"[{self.name}] Tokenizing text strings... Sentiment: Positive.")

class RobotController(BaseAi):
    def execute_task(self):
        print(f"[{self.name}] Calculating torque... Arm movement successful.")

models = [
    ComputerVision("CV-Alpha"), 
    NaturalLanguage("GPT-Lite"), 
    RobotController("Mecha-01")
]

print("   INITIATING APEX LAB KERNEL   ")
print("=" * 32)

for model in models:
    model.boot_up()     
    model.execute_task() 
    print("-" * 20)