README

The Blend Images Collection
----------------------------

Blend Images is a commercial stock photography collection. This project started with approximately 100,000 jpeg images in one directory and a csv of metadata for the pictures.

The goal was to gain insights into where the pictures were shot and what subjects are covered.

Python provides a strong tool for parsing the original data to see the categories of subjects and a method for copying the images into separate directories of collections for viewing. 

Using Tableau to visualize the geographic data allows us to better understand the breadth of the collection, and where specific topics were photographed.


The Project 
-----------

Scripts were written using Python 3 to identify images for separate sub-collections based on keywords in the original metadata with geographic attributes.

The 6 collections selected are: beaches, cities, forests, landmarks, mountains, parks.

A Python script reads the original metadata CSV, locates any occurrence of specified keywords, and then writes a new CSV with only those filenames and their locations. The script was adapted for each collection to isolate the specific image category.

The next phase of the project was writing a script to read each collection CSV, and then copy those image files from the master directory of jpegs to their own separate folders.

A try-except clause returns the filenames of any images that are not found in the master directory (csvcopyfiles.py)

Looking at the images in each collection gives an assessment of keyword accuracy.

Approximately 17% of images were identified for more than one of these collections.

Geocoding latitude and longitude from location name strings was accomplished through Google's Geocoding API.

A Python script was written to combine all of the sub-collection CSVs and then eliminate any duplicate filenames and write out a CSV of unique filenames and locations. This CSV was used for one data visualization of combined collections location data. Some filenames were identified for multiple collections (ie landmarks and parks).

Visualizations were created in Tableau for each collection, using size bubbles to indicate how many images were shot in each global location. And one visualization was created for the aggregate of these sub-collections.


