image_byte_matrix = []

# come back to this project
with open("./inputimages/jamaicaflag.jpg", 'rb') as image:
    for line in image:
        image_byte_matrix.append(list(line))



for row in image_byte_matrix:
    print(row)
