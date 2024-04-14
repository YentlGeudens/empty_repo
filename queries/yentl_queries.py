activity_query = ("select activity_id, activity_type, activity_name, description from cozy_stay.activity "
                  "where activity_type like %s and activity_name like %s;")

booking_query = "select room, max_people from cozy_stay.booking;"