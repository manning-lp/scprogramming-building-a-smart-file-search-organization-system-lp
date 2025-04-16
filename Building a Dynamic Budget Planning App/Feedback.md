## Milestone 1

- Not a required change, but while True/break is often considered bad practice. It might be better to show an approach that exits the while loop based on a condition

ex:
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
