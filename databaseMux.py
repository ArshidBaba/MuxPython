import pickle
import os 
from psycopg2 import Error
import psycopg2


with open('playback_ids.txt', 'rb') as file:
    streams = pickle.loads(file.read())

print(streams)
print(type(streams))
print(streams['Sm7qN907JQg'])
# for key, value in streams.items():
#     print(key, value)
def updateInBulk(records):
    try:
        connection = psycopg2.connect(user = os.environ.get('DB_USER'),
                                    password = os.environ.get('DB_PASSWORD'),
                                    host = os.environ.get('HOST'),
                                    port = os.environ.get('PORT'),
                                    database = os.environ.get('DATABASE'))

        cursor = connection.cursor()

        update_streamurl_query = '''UPDATE live_lecture set stream_url = %s where video_id = %s'''
                                    

        # record_to_insert = (streams['Sm7qN907JQg'],'14dWQYIm_8s')
        cursor.executemany(update_streamurl_query, records)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into lecture table")

        # print("Successfully inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data", error)
    finally:
        #closing database connection
        if(connection):
            cursor.close()
            connection.close()
            print('PostgreSQL connection closed')

records = []
for key, value in streams.items():
    records.append((value, key))



updateInBulk(records)
print(records)