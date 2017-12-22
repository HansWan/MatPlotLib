import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep simulating random walk if the program is active
while True:
    # Create an instance for RandomWalk and draw points
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    # Set screen size
    plt.figure(figsize=(20, 12))
    
    point_numbers = list(range(rw.num_points))
#    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor='none', s = 1)
    plt.plot(rw.x_values, rw.y_values)
    
    # Highlight start point and end point
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
    
    # Hide axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
