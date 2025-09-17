"""
Author: Anna Monaghan
Course: CSCI 3725
Assignment: M1 - A Markov Distinction
Modified: 9/16/25

This system creates a sequence of images using Markov probabilities. Each image has a designated color family,
and the Markov chain determines how likely one color family is to follow another in the sequence. First, a 
sequence of colors is created, and then for each color in the sequence, a photo is chosen at random from the
color's list of images. The system also has plot_sequence and visualize_sequence functions, which allow viewing
of the image sequence as a plot or in a grid series, respectively.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

# A dictionary containing all images and their designated color families
COLOR_GROUPS = {
    "orange" : ["orn1.JPG", "orn2.JPG", "orn3.jpeg", "orn4.jpeg", "orn5.jpeg"],
    "yellow" : ["yel1.jpeg", "yel2.jpeg", "yel3.jpeg", "yel4.jpeg", "yel5.jpeg"],
    "green" : ["grn1.jpeg", "grn2.jpeg", "grn3.jpeg", "grn4.jpeg", "grn5.JPG"],
    "blue" : ["blu1.jpeg", "blu2.jpeg", "blu3.jpeg", "blu4.jpeg", "blu5.jpeg"],
    "purple" : ["pur1.JPG", "pur2.jpeg", "pur3.jpeg", "pur4.jpeg", "pur5.jpeg"],
    "white" : ["whi1.jpeg", "whi2.jpeg", "whi3.jpeg", "whi4.JPG", "whi5.jpeg"],
    "brown" : ["brn1.jpeg", "brn2.jpeg", "brn3.jpeg", "brn4.jpeg", "brn5.jpeg"]
}

class MarkovPhotos:
    """This class creates and visualizes a sequence of images, using the given transition matrix to create
    the color sequence. This class also allows visualization of the sequence as a plot or as an image series.
    """

    def __init__(self, transition_matrix):
        """Initializes MarkovPhotos with the given transition matrix, and creates a list of colors."""
        self.transition_matrix = transition_matrix
        self.colors = list(transition_matrix.keys())

    def get_next_color(self, current_color):
        """A helper method for create_sequence() that returns the next color in the sequence based on the current
        color.
        """
        return np.random.choice(
            self.colors,
            p=[self.transition_matrix[current_color][next_color] for next_color in self.colors]
        )
    
    def choose_photo(self, color_family):
        """A helper method for create_sequence(). Randomly chooses and returns an image from the given
        color family.
        """
        photo = np.random.choice(COLOR_GROUPS[color_family])
        return photo

    def create_sequence(self, current_color="white", sequence_length=16):
        """A method that takes in a given starting color and sequence length, and returns a sequence of that
        many color families.
        """
        color_sequence = [current_color]
        image_sequence = []

        # Make the sequence of color families
        while len(color_sequence) < sequence_length:
            next_color = self.get_next_color(current_color)
            color_sequence.append(next_color)
            current_color = next_color
        
        # Translate the sequence from colors to images of those colors
        for color in color_sequence:
            image = self.choose_photo(color)
            image_sequence.append("photos/" + image)

        return image_sequence
    
    def plot_sequence(self, sequence):
        """Takes in a sequence of images, and creates a plot of where each image falls in the sequence."""
        plt.title("Photo Sequence")
        plt.xlabel("Photo #")
        plt.ylabel("Photo label")
        plt.plot(sequence, drawstyle='steps-post', marker='o')
        plt.show()

    def visualize_sequence(self, image_paths):
        """Takes in a sequence of images, and creates a display of them in order."""
        images = [Image.open(path) for path in image_paths] # Open each image
        fig, axes = plt.subplots(4, 4) # Create a 4 x 4 subplot to display images in a grid
        axes = axes.flatten() # Make the 2D array easier to iterate through

        for i, image in enumerate(images):
            image_fix = ImageOps.exif_transpose(image) # Fix the image rotation at its original point
            axes[i].imshow(image_fix)
            #axes[i].set_title(f"Image {i + 1}")
            axes[i].axis('off')
        plt.tight_layout()
        plt.show()
           
def main():
    transitions = {
        "orange" : {"orange" : 0.3, "yellow" : 0.2, "green" : 0.12, "blue" : 0.1, "purple" : 0.05, "white" : 0.08, "brown" : 0.15},
        "yellow" : {"orange" : 0.15, "yellow" : 0.3, "green" : 0.2, "blue" : 0.1, "purple" : 0.05, "white" : 0.12, "brown" : 0.08},
        "green" : {"orange" : 0.1, "yellow" : 0.15, "green" : 0.3, "blue" : 0.2, "purple" : 0.12, "white" : 0.08, "brown" : 0.05},
        "blue" : {"orange" : 0.08, "yellow" : 0.1, "green" : 0.12, "blue" : 0.3, "purple" : 0.2, "white" : 0.15, "brown" : 0.05},
        "purple" : {"orange" : 0.05, "yellow" : 0.08, "green" : 0.1, "blue" : 0.15, "purple" : 0.3, "white" : 0.2, "brown" : 0.12},
        "white" : {"orange" : 0.05, "yellow" : 0.08, "green" : 0.1, "blue" : 0.15, "purple" : 0.12, "white" : 0.3, "brown" : 0.2},
        "brown" : {"orange" : 0.2, "yellow" : 0.1, "green" : 0.12, "blue" : 0.08, "purple" : 0.05, "white" : 0.15, "brown" : 0.3}
    }

    sequence = MarkovPhotos(transitions)
    images = sequence.create_sequence("green")
    sequence.plot_sequence(images)
    sequence.visualize_sequence(images)


if __name__ == "__main__":
    main()