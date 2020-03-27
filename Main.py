import csv


print("----")
print("my-albums-sorted")
print("OPTIONS: album, artist, date")
print("Type which option you want and press enter")
sort_setting = input()
print("----")

with open("albums.csv", "r") as csvfile_read:
	csv_dictreader = csv.DictReader(csvfile_read, delimiter=";")
	sorted_albums = sorted(csv_dictreader, key=lambda row : row[sort_setting].lower())
	print("Albums sorted by " + sort_setting)

	with open("sortedalbums.csv", "w") as csvfile_write:
		csv_dictwriter = csv.DictWriter(csvfile_write, fieldnames=["album", "artist", "date"], delimiter=";")
		csv_dictwriter.writeheader()
		for line in sorted_albums:
			csv_dictwriter.writerow(line)
		print("Albums printed to sortedalbums.csv")


print()