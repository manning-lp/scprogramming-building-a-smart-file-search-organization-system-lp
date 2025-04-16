def get_total_budget():
  inputDone = False
  total_income = 0

  while not inputDone:
      try:
        total_income = float(input("Enter your monthly income: "))

        if total_income >= 0:
            inputDone = True
      except:
          print("Please enter a float!")

  return total_income

def get_categories():
  categories = []
  inputDone = False

  while not inputDone:
     name = input("Category name (leave blank to finish): ").strip()
     if not name:
        inputDone = True
     else:
        try:
           min_expense = float(input("Enter minimum expense: "))
           categories.append({"Category":name, "Minimum Expense": min_expense})
        except:
           print("Invalid expense, try again")
  
  return categories
           

