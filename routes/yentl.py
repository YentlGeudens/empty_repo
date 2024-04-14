from fastapi import APIRouter
import database
from models import models
from queries import yentl_queries as queries

app = APIRouter()


@app.get("/activities")
def get_activity(type : str = '%', name : str = '%'):
    query = queries.activity_query
    activities = database.execute_sql_query(query, (type, '%{}%'.format(name)))
    if isinstance(activities, Exception):
        return activities, 500
    activities_to_return = []
    for activity in activities:
        activity_dictionary = {"id": activity[0],
                            "type": activity[1],
                            "name": activity[2],
                            "description": activity[3]}
        activities_to_return.append(activity_dictionary)
    return({'activity': activities_to_return})


@app.get("/booking")
def get_all_rooms():
    query = queries.booking_query
    rooms = database.execute_sql_query(query)
    if isinstance(rooms, Exception):
        return rooms, 500
    rooms_to_return = []
    for room in rooms:
        room_info = {'room': room[0], 'max_people': room[1]}
        rooms_to_return.append(room_info)
    return {'rooms': rooms_to_return}