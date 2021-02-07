colors = ["Red", "Green", "Blue", "Orange"]

for color in colors:
    print(f"The color is: {color}")


for num in range(5):
    print(f"The number is: {num}")


for num in range(1, 5):
    print(f"The number is: {num}")

for num in range(2, 11, 2):
    print(f"The number is: {num}")


hex_colors = {
    "Red": "#FF",
    "Green": "#008",
    "Blue": "#0000FF",
}
for color in hex_colors:
    print(f"The value of color is actually: {color}")

for color, hex_value in hex_colors.items():
    print(f"For color {color}, the hex value is: {hex_value}")


if 3 < 5:
    print("If")

if 5 < 3:
    print()
else: 
    print("Else")

if 1 != 1:
    print()
elif 1 == 1:
    print("Elif")
else:
    print()


counter = 0
max = 4

while counter < max:
    print(f"The count is: {counter}")
    counter = counter + 1






