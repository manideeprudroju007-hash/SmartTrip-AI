from tools.tavily_tool import Tavily_Search
from tools.flight_tool import search_flights

#res = Tavily_Search("Best travel destinations in Europe")
#print(res)

res = search_flights("Plan a 7 days Japan trip from Bangladesh")
print(res)