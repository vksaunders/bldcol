# bldcol
Blend Images is a collection of approximately 100k photographs covering a range of subjects, shot by hundreds of photographers based around the world. Using one directory of all of the images and one CSV of metadata, I will use Python to identify specific subjects within the collection through identification of text attributes in the captions and keywords, and then separate these files into separate sub-collections. The geographic locations of these sub-collections will be visualized using Tableau to further explore and understand the range of assets in the Blend collection.

Project steps (using Python):
- Search captions and keywords for themes with geographic implications (ie beaches, tourist attractions, travel destinations, mountain ranges), count the assets in potential collections to make sure the number of photos is meaningful for an actual sub-collection, examine how many distinct locations are represented in potential sub-collections

- Create separate CSVs of the metadata for these sub-collections

- Physically move or copy the images into separate directories for visual understanding of how the images match up with location keywords and see what the collections look like

Project Visualization (using Tableau):
-Use Google Developer geocoding tool to obtain long-lat data for images from string location names

-Global Map Visualization of separate image locations for each sub-collection, with option to turn different collections on-off to understand the breadth of each sub-collection, as well as breadth of all of the geographic collections together.
