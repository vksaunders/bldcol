README

File list
------------
Bldbeaches.py		Read master csv, find all filenames tagged w beach keywords, write new csv
Bldcityscapes.py	Read master csv, find all filenames tagged w city keywords, write new csv
Bldforests.py		Read master csv, find all filenames tagged w forest keywords, write new csv
Bldlandmarks.py	Read master csv, find all filenames tagged w landmark keywords, write new csv
Bldmountains.py	Read master csv, find all filenames tagged w mountain keywords, write new csv
Bldparks.py		Read master csv, find all filenames tagged w park keywords, write new csv
Combinecsv.py		Combine the csvs of these separate collections into one csv
Csvcopyfiles.py		Copy jpg files from master directory to separate collection directories, w csv list
Jpgscopy.py		Copy all jpgs from one directory into another
Jpgsmove.py		Move all jpgs from one directory into another

The Project 
-----------
Blend Images is a commercial stock photography collection. This project started with approximately 100,000 jpeg images in one directory and a csv of metadata for the pictures.

Scripts were written using Python 3 to identify images for separate collections based on keywords with geographic attributes.

The 6 collections selected are: beaches, cities, forests, landmarks, mountains, parks.

Csvs of metadata including the filename and image location were written for each collection.

Using each csv, each collection’s images were copied into new separate directories. A try-except clause returns the filenames of any images that are not found in the master directory (csvcopyfiles.py)

Looking at the images in each collection gives an assessment of keyword accuracy.

Approximately 17% of images were identified for more than one of these collections.

