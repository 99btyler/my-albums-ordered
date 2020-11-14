import csv


print("----")
print("my-albums-ordered")
print("OPTIONS: album, artist, date")
print("Type which option you want and press enter")
sort_setting = input()
print("----")

# Select albums.csv
with open("albums.csv", "r") as csvfile:

	# Read albums.csv content
	csvfile_read = csv.DictReader(csvfile, delimiter=";")

	# Sort content by sort_setting
	sorted_albums = sorted(csvfile_read, key=lambda row : row[sort_setting])
	print("Sorted the albums by " + sort_setting)

	# Write sorted content to sortedalbums.csv
	with open("sortedalbums.csv", "w") as csvfile:
		csvfile_write = csv.DictWriter(csvfile, delimiter=";", fieldnames=["album", "artist", "date"])
		csvfile_write.writeheader()
		for row in sorted_albums:
			csvfile_write.writerow(row)
		print("Printed the sorted albums to sortedalbums.csv")


print()