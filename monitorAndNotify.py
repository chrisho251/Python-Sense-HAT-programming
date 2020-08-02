from environment import temperature

#Create a connection between raspberry and database
connection = MySQLdb.connect("localhost", "pi", "raspberry", "raspberrydb")

with connection.cursor() as cursor:
