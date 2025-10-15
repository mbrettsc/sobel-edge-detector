import sys
import os
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = "output/"


def plot_image(image: np.ndarray) -> None:
    """
    Plots a grayscale image.

    :param image: 2D numpy array representing the grayscale image.
    :type image: np.ndarray
    :return: None
    :rtype: None
    """
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def print_usage() -> None:
    """
    Prints the usage instructions for the script.

    :return: None
    :rtype: None
    """
    print("Usage: python main.py <file_path/my_image.jpg>")

def check_args(args: list) -> None:
    """
    Checks the command line arguments for validity.
    
    :param args: List of command line arguments.
    :type args: list
    :return: None
    :rtype: None
    """
    if len(args) < 2:
        raise ValueError("Missing image path.")
    elif not args[1].endswith(('.jpg', '.png')):
        raise ValueError("The argument must be a .jpg or .png file.")
    else:
        print("File argument accepted.")

def sobel_operator(image: np.ndarray) -> np.ndarray:
    """
    Applies the Sobel operator to a grayscale image to detect edges.

    :param image: 2D numpy array representing the grayscale image.
    :type image: np.ndarray
    :return: 2D numpy array representing the gradient magnitude of the image.
    :rtype: np.ndarray
    """
    Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    Gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    rows, cols = image.shape[:2]
    gradient_magnitude = np.zeros((rows, cols))

    # Convolution with Sobel filters 
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            gx = np.sum(np.multiply(Gx, image[i-1:i+2, j-1:j+2]))
            gy = np.sum(np.multiply(Gy, image[i-1:i+2, j-1:j+2]))
            gradient_magnitude[i, j] = np.sqrt(gx**2 + gy**2)

    # Normalize to range [0, 1]
    return gradient_magnitude / gradient_magnitude.max()

def read_file(file_path: str) -> np.ndarray:
    """
    Reads an image file and converts it to a normalized grayscale image.

    :param file_path: Path to the image file.
    :type file_path: str
    :return: 2D numpy array representing the normalized grayscale image.
    :rtype: np.ndarray
    """
    image = plt.imread(file_path)
    if image.ndim == 3:
        image = image.mean(axis=2)
    image = image.astype(float)
    if image.max() > 1.0:
        image /= 255.0
    return image

def threshold_edges(grad: np.ndarray, threshold: float = 0.3) -> np.ndarray:
    """
    Applies a threshold to the gradient magnitude image to create a binary edge map.

    :param grad: 2D numpy array representing the gradient magnitude of the image.
    :type grad: np.ndarray
    :param threshold: Threshold value to determine edges, defaults to 0.3.
    :type threshold: float, optional
    :return: 2D numpy array representing the binary edge map.
    :rtype: np.ndarray
    """
    return (grad > threshold).astype(float)

def save_to_file(data: np.ndarray, output_path: str) -> None:
    """
    Saves the thresholded edge map to a text file.

    :param data: 2D numpy array to save.
    :type data: np.ndarray
    :param output_path: Path to the output text file.
    :type output_path: str
    :return: None
    :rtype: None
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    output_path = "output/" + output_path + ".txt"
    np.savetxt(output_path, data, fmt='%.3f')
    print(f"Edge map saved to {output_path}")

def get_user_threshold() -> float:
    """
    Continuously prompts the user for a valid threshold value.

    :return: A valid float threshold between 0 and 1.
    :rtype: float
    """
    while True:
        try:
            threshold = float(input("Enter threshold value (0-1): "))
            if 0 <= threshold <= 1:
                return threshold
            else:
                print("Threshold must be between 0 and 1.")
        except ValueError:
            print("Please enter a valid numeric value.")

def analyze_edges(edge_map: np.ndarray) -> list:
    """
    Analyzes and returns basic statistics from the edge map.

    :param edge_map: Binary edge map.
    :type edge_map: np.ndarray
    :return: List of tuples containing statistic names and values.
    :rtype: list
    """
    stats = []
    stats.append(("mean", float(np.mean(edge_map))))
    stats.append(("max", float(np.max(edge_map))))
    stats.append(("min", float(np.min(edge_map))))
    print("Edge Statistics:")
    for stat in stats:
        print(f"{stat[0]}: {stat[1]:.3f}")
    print(f"First statistic: {stats[0]}")
    stats.pop()
    print(f"After pop: {stats}")
    return stats

def main() -> None:
    """
    Main execution function for Sobel edge detection.
    """
    try:
        args = sys.argv
        check_args(args)

        image = read_file(args[1])
        threshold = get_user_threshold()

        grad = sobel_operator(image)
        edges = threshold_edges(grad, threshold)

        plot_image(edges)
        analyze_edges(edges)

        output_name = input("Enter output filename (without extension): ")
        save_to_file(edges, output_name)

    except Exception as e:
        print("Error:", e)
        print_usage()

if __name__ == "__main__":
    main()
