import os

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  spacing = 2

  for row_index in range(num_rings):
    row = ""

    for tower_num, rings in towers.items():
      row += get_ring_display(row_index, rings)

      if int(tower_num) < 3:
        row += (" " * spacing)

    print(row)

  base = "*" * (largest_ring * 3 + spacing * 2)
  print(base)

  labels = ""
  padding = largest_ring // 2

  for tower_num in range(1, 4):
    labels += (" " * padding) + str(tower_num) + (" " * padding)

    if tower_num < 3:
      labels += (" " * spacing)

  print(f"{labels}\n")

def get_ring_display(row_index, rings):
  ring_index = num_rings - (row_index + 1)

  if ring_index >= len(rings):
    padding = largest_ring // 2
    return (" " * padding) + "|" + (" " * padding)
  else:
    ring = rings[ring_index]
    padding = (largest_ring - ring) // 2
    return (" " * padding) + ("-" * ring) + (" " * padding)

def get_num_rings():
  while True:
    num_rings = input("How many rings [2-10]? ")

    if num_rings not in [str(i) for i in range(2, 11)]:
      print("Choose 2-10.\n")
    else:
      return int(num_rings)

def get_source_tower():
  while True:
    tower = input("Which tower to get a ring? ")

    if tower not in ["1", "2", "3"]:
      print("Choose 1, 2, or 3.\n")
    elif len(towers[tower]) == 0:
      print(f"Tower {tower} has no rings.\n")
    else:
      return tower

def get_destination_tower(source_tower):
  while True:
    tower = input("Which tower to move the ring? ")

    if tower not in ["1", "2", "3"]:
      print("Choose 1, 2, or 3.\n")
    else:
      source = towers[source_tower]
      destination = towers[tower]

      if len(destination) == 0 or source[-1] < destination[-1]:
        return tower
      else:
        return None

cls()
print()

print("Move all of the rings to the last rod by moving one ring at a time. Larger rings cannot be placed on smaller rings.\n")

num_rings = get_num_rings()

rings = [i * 2 - 1 for i in range(num_rings, 0, -1)]
largest_ring = rings[0]

towers = {
  "1": rings,
  "2": [],
  "3": []
}

num_moves = 0

while len(towers["3"]) < num_rings:
  print_game_state()

  source_tower = get_source_tower()
  destination_tower = get_destination_tower(source_tower)

  while destination_tower is None:
    print(f"Invalid move.\n")
    source_tower = get_source_tower()
    destination_tower = get_destination_tower(source_tower)

  ring = towers[source_tower].pop()
  towers[destination_tower].append(ring)
  num_moves += 1

print_game_state()
print(f"You solved the puzzle in {num_moves} moves!")
