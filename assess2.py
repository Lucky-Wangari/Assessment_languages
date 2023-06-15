# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity

   
# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average(self):
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)

    def if_passed(self):
        average_grade = self.calculate_average()
        return average_grade >= 60


# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

class FlightBooking:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def flights_search(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights

    def confirm(self, flight,):
        confirmation = f"{flight.destination} {flight.date}"
        return confirmation


class Flight:
    def __init__(self, destination, date, seats):
        self.destination = destination
        self.date = date
        self.available_seats = seats
        self.passenger_list = []

# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
class Library:
    def __init__(self,catalogue,management):
        self.catalogue = catalogue
        self.management=  management
        
    def add_new_book(self):
        self.catalogue
        
    
        
# Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Story:
    def __init__(self, title, content, moral_lesson, age_group):
        self.title = title
        self.content = content
        self.moral_lesson = moral_lesson
        self.age_group = age_group


class StoryTeller:
    def __init__(self, name):
        self.name = name
        self.stories = []

    def adding_story(self, story):
        self.stories.append(story)

    def telling_story(self, story_title):
        for story in self.stories:
            if story.title == story_title:
                 return f"Story found."


class Translate:
    def __init__(self, source, language):
        self.source = source
        self.language = language

    def translation(self):
        return f"Translated text"


# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and

class Recipe:
    def __init__(self, name, ingredients, preparation, cooking, nutrition):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.cooking = cooking
        self.nutritional= nutrition

    def cook(self):
        print(f"Cooking {self.name}")
        
class Moroccan:
    def __init__(self,name,ingredients, preparation, cooking, nutrition):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.cooking = cooking
        self.nutritional= nutrition
        
    def dish(self):
        if self.name == self.ingredients & self.preparation == self.cooking:
            return f"this is Moroccan cuisine"
 
class Ethiopian:
    def __init__(self,name,ingredients, preparation, cooking, nutrition):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.cooking = cooking
        self.nutritional= nutrition
        
    def dish(self):
        if self.name == self.ingredients & self.preparation == self.cooking:
            return f"this is Ethiopian cuisine"
        
class Nigerian:
    def __init__(self,name,ingredients, preparation, cooking, nutrition):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.cooking = cooking
        self.nutritional= nutrition
        
    def dish(self):
        if self.name == self.ingredients & self.preparation == self.cooking:
            return f"this is Nigerian cuisine"
    
       
       







        

        
        