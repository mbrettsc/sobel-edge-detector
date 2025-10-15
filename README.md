
# Sobel Edge Detection in Python

This project implements a simple edge detection program using the Sobel operator, a classic image processing technique used to highlight areas of rapid intensity change, i.e., edges.  
The user provides an image (in .jpg or .png format), chooses a threshold value, and the program detects edges, visualizes them, and saves the result to a text file.

## Features

1.  Reads and converts an image into grayscale.
2.  Applies horizontal and vertical Sobel kernels to detect changes in intensity along both directions.
3.  Combines both gradients to compute the edge magnitude.
4.  Applies a threshold (chosen by the user) to produce a binary edge map.
5.  Displays the resulting edges visually.
6.  Saves the binary edge map to a text file.
7.  Calculates and displays basic statistics (mean, min, max) for the detected edges.
8.  
## How to use it:
Run the program from the terminal:

```python
python main.py path/to/your/image.jpg
```
Then follow the prompts:

-   Enter a threshold value between 0 and 1.
-   View the resulting edge-detected image.
-   Enter a name to save the output file (saved inside the output/ folder).
    
## Acknowledgements and References

### Conceptual references:
    
-   Fisher R, Perkins S, Walker A, Wolfart E (1996)  Hypermedia  image processing reference. John Wiley & Sons Ltd, England, pp 183–202
 ©2003 University of Edinburgh — [HIPR2 Project](https://homepages.inf.ed.ac.uk/rbf/HIPR2/sobel.htm)
### Code references:

-   The implementation of Sobel convolution and edge magnitude calculation was written entirely by Martin Brettschneider.
    
## Authorship Statement

I declare that all code and documentation in this repository are **my own work**.  
No generative AI tools were used to produce any code or text.  
All conceptual and code inspirations are properly cited.  
This work adheres to the **Radboud University** course and conduct standards.

## Author

**Martin Brettschneider**  
📧 [martin.brettschneider@ru.nl](mailto:martin.brettschneider@ru.nl)  
🔗 [ResearchGate Profile](https://www.researchgate.net/profile/Martin-Brettschneider-2?ev=hdr_xprf)


## 📄 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
