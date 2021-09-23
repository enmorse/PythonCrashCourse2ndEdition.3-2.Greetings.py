# Start with the list you used in Exercise 3-1,
# but instead of just printing each person's name,
# print a message to them.
# The text of each message should be the same,
# but each message should be personalized with the
# person's name.

names = ["john", "nate", "vincent"]

message1 = f"What's up {names[0].title()}? It is good " \
           f"to see you bro!"
message2 = f"What's up {names[1].title()}? It is good " \
           f"to see you bro!"
message3 = f"What's up {names[2].title()}? It is good " \
           f"to see you bro!"

print(message1)
print(message2)
print(message3)
