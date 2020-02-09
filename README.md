# dataproc

## Installation

You can download the current development version by cloning this repository

	$ git clone https://github.com/duckrojo/dataproc 

## Testing

Running tests is done by directly calling pytest from the root folder of the project
	
	$ pytest

## Documentation

You can compile the autogenerated documentation using the following command from the
docs directory

	$ cd docs
	$ make html

## Dependencies

dataproc supports python version 3.7 or higher, it currently depends on the following libraries: 

* astropy 
* numpy 
* astroquery 0.3.10 or higher 
* scipy 
* matplotlib 
* pyephem
