import csv


with open("albums.csv", "r") as albumsfile:

	albumsfile_read = csv.DictReader(albumsfile, delimiter=";")

	print("----")
	print("my-albums-ordered")
	print("OPTIONS:")
	options = albumsfile_read.fieldnames
	for i in range(len(options)):
		print(f"{i}. '{options[i]}'")
	print("Which one do you want to sort by?")
	# Get decision
	while True:
		# - make sure it's a number
		try:
			decision = int(input("Enter number: "))
		except ValueError:
			continue
		# - make sure it's valid
		if decision >= 0 and decision < len(options):
			break
	sort_setting = options[decision]
	print(f"You selected '{sort_setting}'")

	sorted_albums = sorted(albumsfile_read, key=lambda row : row[sort_setting])
	print(f"Sorted the albums by {sort_setting}")

	with open("albums.csv", "w") as albumsfile:
		albumsfile_write = csv.DictWriter(albumsfile, delimiter=";", fieldnames=options)
		albumsfile_write.writeheader()
		for row in sorted_albums:
			albumsfile_write.writerow(row)
		print(f"Printed the albums by {sort_setting}")

