Title: MakingMarkovPhotoSequences

Set-up and run: To run this system, you will need an IDE with numpy, matplotlib.pyplot, and PIL.
Ensure that the photos folder is in your directory along with the code file, and then run the file.
During running, the plot will show up first. Once you have closed it, the image sequence will load.
That's all there is to it! The 5 outputs (2 plots and 3 series) can be found in the "Products" folder
(Plot_3 corresponds to Series_3).

Description: This system creates sequences of images based on Markov probabilities.
The images are all photos that I have taken myself, and I grouped them according to what color I felt
was most dominant in the image. The transition matrix for this system is based on these color groupings,
with the hope that the resulting sequence has smooth color transitions.

This system is meaningful to me because I am getting to use my passion for photography and incorporate
it into my interest in computer science. I travel a lot with my family, and the photographs that I take
on these trips are meaningful reminders to me of the invaluable experiences that I have had, and the 
beautiful places I have been able to see. Not only are photos a way for me to remind myself of my love 
for people and places, but they also allow me to express myself and my viewpoint of a place. Often,
photographs give us vital insight into who a person is, and how they see the world, and I hope that my
photos do the same.

Building this system challenged me to use multiple libraries and concepts that I had never encountered before,
including numpy, matplotlib, and Markov chains. These were important challenges for me because I tend not to have
confidence in my programming abilities, and coming off of two full semesters of theory-heavy classes with little
to no programming in them, I was feeling especially rusty and unsure. Creating this system challenged me to
remember my programming skills and practices, and learn how to incorporate multiple new elements into my programs.
Going forward, I would like to continue to use new libraries, and push myself to be able to build simple systems
without referencing class materials or code that I have already written.

I think this system is creative in some ways. I think that the product it creates is creative and fun, but I
hesitate to necessarily call the system creative because a lot of the decision-making is done by the
programmer. I chose all of the photos that the system uses, and grouped them according to color. I think the
parts of the system that are creative are when it chooses the sequence of colors, and when it chooses which
photograph should correspond to each color in the sequence.

Thank you to Professor Harmon for much debugging advice and idea brainstorming, and this Pillow documentation
page (https://pillow.readthedocs.io/en/stable/reference/ImageOps.html) for helping me learn about the ImageOps
module, and correcting image rotation!