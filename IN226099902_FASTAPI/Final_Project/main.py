from fastapi import FastAPI, Query, Response, status,HTTPException
from pydantic import BaseModel, Feild
from typing import List

app=FastAPI()

####*******Models Pydantic validate incoming requests data automatic******######
class BookingRequest(BaseModel):
    customer_name:str=Field(...,min_length=2)
    movie_id:int=Field(...,gt=0)
    seats:int=Field(...,gt=0,le=10)
    phone:str=Feild(...,min_length=10)
    seat_type:str="standard"
    promo_code:str=""

class NewMovie(BaseModel):
    title:str=Feild(...,min_length=2)
    genre:str=Feild(...,min_length=2)
    language:str=Feild(...,min_length=2)
    duration_mins:int=Feild(...,gt=0)
    ticket_price:int=Feild(...,gt=0)
    seats_available:int=Feild(...,gt=0)

class SeatHold(BaseModel):
    customer_name:str
    movie_id:int
    seats:int

####Data ==Stoes movies, bookings
movies=[
    {"id":1,"title":"Avengers","genre":"Action","Language":"English","duration_mins":150,"ticket_price":300,"seats_available":390}
    {"id":2,"title":"Conjuring","genre":"Horror","Language":"English","duration_mins":180,"ticket_price":380,"seats_available":230}
    {"id":3,"title":"Pushpa","genre":"Action","Language":"Hindi","duration_mins":140,"ticket_price":400,"seats_available":310}
    {"id":4,"title":"Golmaal","genre":"Comedy","Language":"Hindi","duration_mins":160,"ticket_price":320,"seats_available":210}
    {"id":5,"title":"KGF Chapter1","genre":"Action","Language":"Kannada","duration_mins":180,"ticket_price":290,"seats_available":180}
    {"id":6,"title":"Kantara","genre":"Horror","Language":"Hindi","duration_mins":140,"ticket_price":310,"seats_available":100}
    {"id":7,"title":"Dhurandhar","genre":"Action","Language":"Hindi","duration_mins":190,"ticket_price":410,"seats_available":300}
]
bookings=[]
holds=[]

booking_counter=1
hold_counter=1

# Helpers used for reusable business logic fun
def find_movie(movie_id:int):
    for m in movies:
        if m["id"]==movie_id:
            return m
        return None

def calculate_ticket_cost(price,seats,seat_type,promo_code):
    multiplier=1
    if seat_type=="premium":
        multiplier=1.5
    elif seat_type=="recliner":
        multiplier=2

    original=price*seats*multiplier

    discount=0
    if promo_code=="SAVE10":
        discount=original*0.1
    elif promo_code=="SAVE20":
        discount=original*0.2
    
    return int(original),int(original-discount)

def filter_movies_logic(genre=None,language=None,max_price=None,min_seats=None):
    result=movies
    if genre is not None:
        result=[m for m in result if m["genre"]==genre]
    if language is not None:
        result=[m for m in result if m["langauge"]==language]
    if max_price is not None:
        result=[m for m in result if m["max_price"]==max_price]
    if min_seats is not None:
        result=[m for m in result if m["min_seats"]==min_seats]


###Question1 HOME
#API is running or not confirmed 

@app.get("/")
def home():
    return{"message":"Welcome to CineStar Booking"}

### Question 2 Get All Movies showing total and seats of total

@app.get("/movies")
def get_movies():
    return{
        "movies":movies,
        "total":len(movies),
        "total_seats_available":sum(m["seats_available"] for m in mvoies)
    }

# Question 5 Summary is above id

@app.get("/movies/summary")
def summary():
    return{
        "total_movies":len(movies),
        "most_expensive":max(movies,key=lambda x:x["ticket_price"]),
        "cheapest":min(movies,key=lambda x:x["ticket_price"]),
        "total_seats":sum(m["seats_available"] for m in movies),
        "genre_count":{g:len([m for m in movies if m["genre"]==g]) for g in set(m["genre"] for m in movies)}
    }

# Question 3 Get Movies by id
@app.get("/movies/{movie_id}")
def get_movie_id(movie_id:int):
    movie=find_movie(movie_id)
    if not movie:
        raise HTTPException(404,"Movie not found")
    return movie

# Question 4 Get Booking List
@app.get("/bookings")
def get_bookings():
    return{
        "bookings":bookings,
        "total":len(bookings),
        "total_revenue":sum(b["final_cost"] for b in bookings)
    }
