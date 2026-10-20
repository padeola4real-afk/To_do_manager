# import json, os
# from datetime import datetime, date


# due_date = datetime.strptime("15/10/2026", "%d/%m/%Y").date()
# today = date.today()

# remain = (due_date - today).days
# print(remain)


# # date(2026, 10, 15).isoformat()
# # date.fromisoformat("2026-10-15")

# # print(type(date(2026, 10, 15).isoformat()))
# # print(type(date.fromisoformat("2026-10-15")))
# # def testing():
# #     while True:
# #         typed_input = input("Enter due date (DD/MM/YYYY) or press [Enter] to skip:    ")
# #         if typed_input == "":
# #             return None
# #         try:
# #             due_date = datetime.strptime(typed_input, "%d/%m/%Y")
# #             if due_date.date() < date.today():
# #                 print("Due date can not be in the past")
# #                 continue
# #             else:
# #                 return due_date.date()
                
# #         except ValueError:
# #             print("Invalid Entry!! Write in this exact format: (DD/MM/YYYY)")


# # task = {
# #     "description": "Pay rent",
# #     "due_date": date(2026, 10, 15)
# # }

# # task["due_date"] = task["due_date"].isoformat()
# # print(task)

# # with open("demo.json", "w") as file:
# #         json.dump(task, file, indent=4)


# # with open("demo.json", "r") as file:
# #     loaded = json.load(file)

# # print(type(loaded["due_date"]))      # what type came back?

# # # text -> date, after loading
# # loaded["due_date"] = date.fromisoformat(loaded["due_date"])

# # print(type(loaded["due_date"]))      # and now?
# # print((loaded["due_date"] - date.today()).days)
  




