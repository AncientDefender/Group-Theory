# Group Theory Repository

Welcome to the Group Theory repository! This project delves into the various programs I developed in response to practical needs observed in my daily life, all while reflecting on group theoretical concepts.

## Table of Contents

1. [Files Description](#files-description)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [Notes](#notes)
   
## Files Description:

### `permutation_group_deg_*.txt`:

- These files contain data pertaining to permutation groups of different degrees.
- Each file contains group elements represented as matrices, illustrating the transformations and symmetries within permutation groups.

### `symmetric_groups-retrospective.py`:

- This Python file sets the foundation for retrospective analyses of symmetry groups.
- The script includes functions and methods for constructing symmetric groups over the set {1,2,...,n}.

### `symmetric_groups-ghost_legs.py`:

- This Python file demonstrates the Amidakuji technique on the construction of unique arrangements from finite elements.
- The script includes functions and methods for constructing symmetric groups over the set {1,2,...,n}.

### `combine_colors.py`:
- This custom Python module enhances the management and efficiency of combining ANSI color codes for terminal text formatting.
- It enables the dynamic creation of diverse color combinations, improving the visual aesthetics of your terminal output.

## Usage:

### Data Files (`permutation_group_deg_*.txt`):

- These files can be used for studying the structure and properties of permutation groups of any degree.
- They can be imported into computational tools for further analysis.

### Python Scripts (`symmetric_groups-retrospective.py`, `symmetric_groups-ghost_legs.py`):

- To use the `symmetric_groups-retrospective` and `symmetric_groups-ghost_legs` scripts, ensure you have Python installed (version 3.x).
- Run the script using: `python symmetric_groups-retrospective.py` or `python symmetric_groups-ghost_legs.py`.

### Python Module (`combine_colors.py`):

- To use `combine_colors.py`, import the module into your script to enable advanced color and character formatting for terminal text output.
- The standalone `combine_colors.py` download includes example usage to demonstrate its functionality.

## Features

### `symmetric_groups-retrospective.py`

- **Dynamic Matrix Generation**: Generates new matrices by inserting elements into every possible position in the rows.
- **Timeout**:  Uses multithreading with a timeout to ensure prompt responses and minimize cases when input is delayed.

### `symmetric_groups-ghost_legs.py`

- **Dynamic Matrix Construction**: Builds a matrix to represent permutations using the Amidakuji technique.
- **Formatted Output**: Results are displayed with corresponding symmetric group notation and color-coded formatting.
- **Customized Output**: Permutations are displayed in batches of 1000 with an option to view additional outputs or exit after each batch.

### `combine_colors.py`

- **Dynamic Color Combinations**: Easily combine styles and colors to create custom formatting codes.

## Contributing

Contributions and improvements to the data processing methods are welcome through pull requests.

## Notes:

### Purpose:

- The repository aims to provide resources and tools for studying permutation groups and performing retrospective analyses.

### Data Interpretation:

- Each `permutation_group_deg_*.txt` file contains structured data specific to the degree of its subgroup.
- `permutation_group_deg_11` is available but will not be uploaded here due to its large file size (> 100MB), even after compression.
- Interpret these files in the context of group theory and computational algebraic analysis.

### Script Functionality:

- Review the scripts to understand their functionality and customize them as needed for specific analyses or extensions.

---

Created by KWThunderRaft  
Initial Release: July 12, 2024  
Last Updated: August 2, 2024  
