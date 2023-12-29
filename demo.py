# import pandas as pd

# weather_data = {
#     "area" : ["Goa","Ooty", "Hyderabad"],
#     "temperature" : [35,28,33],
#     "event" : ["Sunny", "Rainy", "Rainy"]
# }
# df = pd.DataFrame(weather_data)
# print(df)



def fun_x(array):
    print(*array)
    for i in range(len(array)):
        print(array[i])
    print([element for element in array])

k = [1,2,3,4]
fun_x(k)