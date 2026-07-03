from tools.tavily_tool import Tavily_Search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res = Tavily_Search("Best travel destinations in Europe")
#print(res)

#res = search_flights("Plan a 7 days Japan trip from Bangladesh")
#print(res)

user_input = input("Enter your travel query: ")

res = run_travel_agent(user_input = user_input, thread_id = "test_user")
print(res["answer"])