mkad=109
speed=int((input("Введите сокрость Васи, км/ч: ")))
t=int((input("Как долго ехал Вася, ч: ")))
dist=int(speed*t)
laps=int(dist//mkad)
if dist<mkad:
	print("Вася остановился на отметке ", dist, "км")
print("Вася остановился на отметке", int(dist-(mkad*laps)), "км")