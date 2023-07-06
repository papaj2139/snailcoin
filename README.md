
# Snailcoin

Snailcoin is a Python library for generating Snailcoin patterns, which consist of black (0) and white (1) pixels. It is designed to be used for world generation in pycord projects.

## Installation

You can install Snailcoin using `pip`:

pip install snailcoin



## Usage

Here's a basic example of how to use Snailcoin to generate a Snailcoin pattern:

```python
from snailcoin import generate_snailcoin_noise

width = 100
height = 100
scale = 10

snailcoin = generate_snailcoin_noise(width, height, scale)

# Display the generated Snailcoin pattern
for row in snailcoin:
    line = ''.join(['#' if val == 1 else '.' for val in row])
    print(line)
In this example, we import the generate_snailcoin_noise function from the Snailcoin library. We then define the width, height, and scale of the pattern. Finally, we generate the Snailcoin pattern and display it on the console.
