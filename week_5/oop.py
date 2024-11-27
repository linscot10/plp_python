
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
    
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price) 
        self.camera_megapixels = camera_megapixels
    
    
    def display_info(self):
        super().display_info()  
        print(f"Camera: {self.camera_megapixels} MP")

    def take_picture(self):
        print(f"Taking a picture with {self.camera_megapixels} MP camera")

basic_phone = Smartphone("Nokia", "3310", 50)
smartphone_with_camera = SmartphoneWithCamera("Apple", "iPhone 14", 999, 12)


print("Basic Phone Info:")
basic_phone.display_info()
print("\nSmartphone with Camera Info:")
smartphone_with_camera.display_info()


basic_phone.make_call("123-456-7890")
smartphone_with_camera.take_picture()



# activity 2


class Animal:
    def move(self):
        pass 

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")


class Bird(Animal):
    def move(self):
        print("Flying 🦅")

dog = Dog()
fish = Fish()
bird = Bird()


animals = [dog, fish, bird]

for animal in animals:
    animal.move()
