print("Title of program: Zhao bot")
print()
while True:
  description = input("Could you describe how you feel, it's alright if u feel not very well maybe i can help?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("its too bad for u,keep crying")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("i do not care:) ")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are weaker than you think")
      counter += 1
    if each_word == "idk":
      feelings_list.append("idk")
      encouragement_list.append("It's alright u are not sure how u feel, do something fun like gaming or exercising!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("U should play go out and do something fun like playing sports and going out with friends!")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use explain it differently to help be understand better."

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
