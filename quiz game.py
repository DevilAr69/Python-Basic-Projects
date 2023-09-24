print("WELCOME! to my world")

playing  = input("Do u want to play? ").lower()

if playing == 'yes':
  print("let's go then :)")
else:
  print("see ya! then")

score = 0

answer = input('What does GPU stand for? ').lower()
if answer == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("incorrect!")
  score += 0

answer = input('What does ROM stand for? ').lower()
if answer == "read only memory":
  print("Correct!")
  score += 1
else:
  print("incorrect!")
  score += 0

answer = input('What does W3 stand for? ').lower()
if answer == "world wide web":
  print("Correct!")
  score += 1
else:
  print("incorrect!")
  score += 0

answer = input('What does HP stand for? ').lower()
if answer == "hewlett_packard":
  print("Correct!")
  score += 1
else:
  print("incorrect!")
  score += 0


print("You got " + str(score) + "question correct!")
print("You got " + str((score/4)*100) + "%.")


