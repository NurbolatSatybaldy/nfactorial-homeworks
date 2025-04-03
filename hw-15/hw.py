import math
import random
from datetime import datetime, timedelta


# Exercise 1: Pizza class
class Pizza:
    def __init__(self):
        self.ingredients = set()

    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError("Duplicate ingredient")
        self.ingredients.add(ingredient)


# Exercise 2: Elevator class
class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def get_current_floor(self):
        return self.current_floor


# Exercise 3: Stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


# Exercise 4: BankAccount class
class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def check_balance(self):
        return self.balance


# Exercise 5: Person class (base for School, etc.)
class Person:
    def __init__(self, name, age=0):
        if age is not None and age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


# Exercise 6: Animal, Dog, Cat classes
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Exercise 7: Calculator class with static methods
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return x / y


# Exercise 8: Car class
class Car:
    def __init__(self, speed, mileage):
        if speed < 0 or mileage < 0:
            raise ValueError("Speed and mileage cannot be negative")
        self.speed = speed
        self.mileage = mileage


# Exercise 9: Course class (for enrollment)
class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            print(student.name)


# Exercise 10: Flight class with departure as a formatted string
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        # Convert departure to a datetime object and store it internally.
        if isinstance(departure, str):
            try:
                # Try parsing as "HH:MM" (using today's date)
                t = datetime.strptime(departure, "%H:%M").time()
                today = datetime.today()
                self._departure = datetime.combine(today.date(), t)
            except ValueError:
                # Otherwise assume ISO format.
                self._departure = datetime.fromisoformat(departure)
        else:
            self._departure = departure
        self.passengers = []

    @property
    def departure(self):
        # Return departure time in "HH:MM" format.
        return self._departure.strftime("%H:%M")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        # Now delay_time is interpreted as hours.
        self._departure += timedelta(hours=delay_time)


# Exercise 11: Library and Book classes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


# Exercise 12: Matrix class
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        if len(self.matrix) != len(other.matrix) or any(
                len(row1) != len(row2) for row1, row2 in zip(self.matrix, other.matrix)):
            raise ValueError("Matrices must have the same dimensions for addition")
        result = []
        for row1, row2 in zip(self.matrix, other.matrix):
            result.append([a + b for a, b in zip(row1, row2)])
        return Matrix(result)

    def subtract(self, other):
        if len(self.matrix) != len(other.matrix) or any(
                len(row1) != len(row2) for row1, row2 in zip(self.matrix, other.matrix)):
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = []
        for row1, row2 in zip(self.matrix, other.matrix):
            result.append([a - b for a, b in zip(row1, row2)])
        return Matrix(result)

    def multiply(self, other):
        n = len(self.matrix)
        m = len(self.matrix[0])
        if m != len(other.matrix):
            raise ValueError(
                "Number of columns of first matrix must equal number of rows of second matrix for multiplication")
        p = len(other.matrix[0])
        result = [[0] * p for _ in range(n)]
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)


# Exercise 13: Rectangle class
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


# Exercise 14: Circle class
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# Exercise 15: Triangle class
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The given sides do not form a valid triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5


# Exercise 16: AbstractShape and derived classes
class AbstractShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class CircleShape(AbstractShape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class RectangleShape(AbstractShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class TriangleShape(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The given sides do not form a valid triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5


# Exercise 17: MusicPlayer class
class MusicPlayer:
    def __init__(self):
        self.playlist = []  # renamed to match test expectations
        self.current_index = 0

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):
        if not self.playlist:
            print("No songs to play")
            return None
        return self.playlist[self.current_index]

    def next_song(self):
        if not self.playlist:
            print("No songs in playlist")
            return None
        self.current_index = (self.current_index + 1) % len(self.playlist)
        return self.playlist[self.current_index]

    def shuffle(self):
        random.shuffle(self.playlist)
        self.current_index = 0

    @property
    def current_song(self):
        if not self.playlist:
            return None
        return self.playlist[self.current_index]


# Exercise 18: Product class
class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot add negative stock")
        self.quantity += quantity

    def sell(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot sell negative quantity")
        if quantity > self.quantity:
            raise ValueError("Not enough stock to sell")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity


# Exercise 19: VideoGame class
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"


# Exercise 20: School with Teacher and Student classes
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Student(Person):
    def __init__(self, name, age=0):
        super().__init__(name, age)


class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def print_all(self):
        for teacher in self.teachers:
            print(f"Teacher: {teacher.name}, Age: {teacher.age}")
        for student in self.students:
            print(f"Student: {student.name}, Age: {student.age}")

    def get_all(self):
        return self.teachers + self.students


# Exercise 21: Card and Deck classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError("No cards left to deal")
        return self.cards.pop()

    def count(self):
        return len(self.cards)
