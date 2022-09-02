students = 10

medias = []

for i in range(1, students + 1):
    notes = 0
    for j in range (1,5):
        notes += float(input("insert the note %i of 4 from the student %i of %i: " %(j,i,students)))

        notes /= 4

        medias.append(notes)

num = 0 

for media in medias:
    if media >= 7.1:
        num += 1

print("Numer of students with media grater then 7 is %i" %num)

