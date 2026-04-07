# # Dictionary
# dict = {
#     "Name" : "Ram",
#     "Age" : 20,
#     "Phone No" : 9876543210,
#     "City" : "Pune"
# }
#
# print(dict["Age"])
#
# for i in dict:
#     print(i)
#     print(dict[i])


# # Student Score Dictionary
# student_scores = {
#     "Ram" : 93,
#     "Kishan" : 83,
#     "Prakash" : 60,
#     "Smit" : 94,
#     "Simran" : 46,
#     "Janvi" : 84,
#     "Herry" : 74
# }
#
# student_grades = {}
#
# for student in student_scores:
#     score = student_scores[student]
#
#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)


# # Nested list in Dictionary
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"]
# }
#
# # Print Lille
# print(travel_log["France"][1])


# nested_list = ["A","B",["C","D"]]
#
# # Print "D"
# print(nested_list[2][1])


travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visites" : 12
    },
    "Germany" : {
        "cities_visited" : ["Stuttgart", "Berlin"],
        "total_visites" : 5
    }
}

# Print "Stuttgart"
print(travel_log["Germany"]["cities_visited"][0])