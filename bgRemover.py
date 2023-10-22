from rembg import remove
from PIL import Image

input_path = input("give me the input path: ")
output_path = input("name your output file: ")
input_pic = Image.open(input_path)
output = remove(input_pic)
output.save(output_path)
