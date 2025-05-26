import requests

api_key = "92251c62b725a9e9a5daace6442334a1"
dict_user_amt = {}
dict_converted_amt = {}
list_curr = []

n = int(input("Enter the number of currency you want to add: "))

for i in range(n):
    user = input("Enter currency to convert to (BASE AMOUNT: EUROS): ").strip().upper()
    amount = int(input("Enter the amount: "))
    dict_user_amt.update({user:amount})
    list_curr.append(user)

symbols = ",".join(list_curr)
url = f"https://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={symbols}"

response = requests.get(url)
data = response.json()

initial_currency_data = {
    "Date" : data["date"],
    "Base": data["base"],
    "Rate":data["rates"]
}

print(f"Date: {initial_currency_data["Date"]}, Base currency: {initial_currency_data["Base"]}, Conversion Rate: {initial_currency_data["Rate"]}")

for key in dict_user_amt: 
    if key in initial_currency_data["Rate"]: 
        dict_converted_amt[key] = dict_user_amt[key] * initial_currency_data["Rate"][key]

for key in dict_converted_amt:
    dict_converted_amt[key] = round(dict_converted_amt[key], 2)

print(f"Converted amount : {dict_converted_amt}")