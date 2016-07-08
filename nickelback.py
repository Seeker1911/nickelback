# Example set
songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

#Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
# for band,song in songs:
# 	print(band)
# 	print(song)

#creates a new tuple 
new_songs = {(band,song) for band,song in songs if band != "Nickelback"}

# comparing index of tuple
rewrite = {item for item in songs if item[0] != 'Nickelback'}
# print(songs)
print(new_songs)
print(rewrite)
