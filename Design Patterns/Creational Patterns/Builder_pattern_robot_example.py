class Robot:
    def __init__(self, head, body, tail, hands, legs):
        self.head = head
        self.body = body
        self.tail = tail
        self.hands = hands
        self.legs = legs
        
    def display_robot(self):
        print("ROBOT:")
        print(f" Head: {self.head}")
        print(f" Body: {self.body}")
        print(f" Hands: {self.hands}")
        print(f" Tail: {self.tail}")
        print(f" Legs: {self.legs}")
    
    class Builder:
        def __init__(self):
            self.head = None
            self.body = None
            self.tail = None
            self.hands = None
            self.legs = None
            
        def set_head(self, head):
            self.head = head
            return self
        
        def set_body(self, body):
            self.body = body
            return self
        
        def set_hands(self, hands):
            self.hands = hands
            return self
        
        def set_tail(self, tail):
            self.tail = tail
            return self
        
        def set_legs(self, legs):
            self.legs = legs
            return self
        
        def build(self):
            return Robot(self.head, self.body, self.hands, self.legs, self.tail)
        
robot = Robot.Builder().set_head("metal").set_body("plastic").set_hands("claws").set_legs("wheels").set_tail("none").build()
robot.display_robot()