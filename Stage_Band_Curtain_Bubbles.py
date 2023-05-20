import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random


class BubbleMachine:
    def __init__(self, pos):
        self.pos = pos
        self.bubbles = []
        self.flow = 1
        self.max_bubbles = 10
        self.bubble_count = 0

    def startBubbles(self):
        self.flow = 1

    def stopBubbles(self):
        self.flow = 0

    def stepChange(self):
        if self.flow == 1 and self.bubble_count < self.max_bubbles:
            self.bubbles.append([self.pos[0], self.pos[1]])
            self.bubble_count += 1

        for s in self.bubbles:
            s[0] = s[0] + 50 * np.random.random() - 5  # Move horizontally with larger random offset (-5 to 5)
            s[1] = s[1] + 50 * np.random.random() - 5  # Move vertically with larger random offset (-5 to 5)

            # Wrap around if bubble goes off the screen
            if s[0] > 500 or s[0] < 0 or s[1] > 500 or s[1] < 0:
                s[0] = self.pos[0]
                s[1] = self.pos[1]

    def plotBubbles(self, ax):
        xvalues = [s[0] for s in self.bubbles]
        yvalues = [s[1] for s in self.bubbles]
        ax.scatter(xvalues, yvalues, c="white", alpha=0.4, s=100)  # Set the bubble size (s) here


def main():
    bubbles = BubbleMachine((0, 200))

    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))

    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
    circle1 = plt.Circle((50, 25), 20, color="red")
    ax0.add_patch(circle1)
    circle2 = plt.Circle((150, 25), 20, color="blue")
    ax0.add_patch(circle2)
    circle3 = plt.Circle((250, 25), 20, color="green")
    ax0.add_patch(circle3)
    circle4 = plt.Circle((350, 25), 20, color="yellow")
    ax0.add_patch(circle4)
    circle5 = plt.Circle((450, 25), 20, color="purple")
    ax0.add_patch(circle5)

    # Add reflection of stage lights
    reflect_rectangle1 = plt.Rectangle((20, 60), 60, 400, color="red", alpha=0.3, zorder=10)
    ax1.add_patch(reflect_rectangle1)
    reflect_rectangle2 = plt.Rectangle((130, 60), 60, 400, color="blue", alpha=0.3, zorder=10)
    ax1.add_patch(reflect_rectangle2)
    reflect_rectangle3 = plt.Rectangle((220, 60), 60, 400, color="green", alpha=0.3, zorder=10)
    ax1.add_patch(reflect_rectangle3)
    reflect_rectangle4 = plt.Rectangle((320, 60), 60, 400, color="yellow", alpha=0.3, zorder=10)
    ax1.add_patch(reflect_rectangle4)
    reflect_rectangle5 = plt.Rectangle((430, 60), 60, 400, color="purple", alpha=0.3, zorder=10)
    ax1.add_patch(reflect_rectangle5)

    # Add 10 circles with the specified properties
    for i in range(10):
        circle = plt.Circle((20 + i * 50, 30), 20, color="yellow", zorder=10)
        ax1.add_patch(circle)

    # Add another curtain object
    curtain = plt.Rectangle((20, 60), 100, 100, color="purple")
    ax1.add_patch(curtain)

    ax1.set_aspect("equal")
    ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color="black")

    rectangle = plt.Rectangle((220, 130), 60, 100, color="gray", zorder=10)
    ax1.add_patch(rectangle)

    # Add a triangle outside the stage with a higher order value
    triangle_vertices = np.array([[225, 250], [275, 250], [250, 300]])
    triangle = plt.Polygon(triangle_vertices, color="orange", zorder=10)
    ax1.add_patch(triangle)

    # Add another circle outside the stage with the same properties as circle6
    circle7 = plt.Circle((30, 150), 30, color="gray", zorder=10)
    ax1.add_patch(circle7)

    rectangle = plt.Rectangle((0, 450), 500, 80, color="red", zorder=10)
    ax1.add_patch(rectangle)

    rectangle = plt.Rectangle((10, 60), 40, 100, color="gray", zorder=10)
    ax1.add_patch(rectangle)

    # Add the stage curtain
    ax1.fill([0, 500, 500, 0], [0, 0, 60, 60], color="blue")

    # Load the image using mpimg.imread()
    image_path = r"D:\MY_WORK\DEVELOPMENT\Python\UpWork\Stage_Simulation\images.jpeg"  # Replace with the actual path 
    # to your image file
    image = mpimg.imread(image_path)

    # Get the size of the screen
    screen_width = ax1.get_xlim()[1]
    screen_height = ax1.get_ylim()[1]

    # Set the desired image size
    image_width = 525
    image_height = 400

    # Calculate the position to center the image on the screen
    image_x = (screen_width - image_width) / 2.5
    image_y = (screen_height - image_height) / 2.5

    # Display the image in front of the screen with adjusted width and height
    ax1.imshow(image, extent=[image_x, image_x + image_width, image_y, image_y + image_height], alpha=0.5, zorder=10)

    # Store the stage lights patches
    stage_lights = [circle1, circle2, circle3, circle4, circle5]
    reflect_rectangles = [reflect_rectangle1, reflect_rectangle2, reflect_rectangle3, reflect_rectangle4,
                          reflect_rectangle5]

    for a in range(300):
        bubbles.stepChange()
        bubbles.plotBubbles(ax1)

        # Change stage light colors randomly
        for light, reflect_rect in zip(stage_lights, reflect_rectangles):
            color = random.choice(["red", "blue", "yellow"])
            light.set_color(color)
            reflect_rect.set_color(color)

        plt.title("Floating Bubble - " + str(a + 1), fontsize="18")
        plt.pause(0.5)

    plt.show()


if __name__ == "__main__":
    main()
