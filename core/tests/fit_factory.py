import astropy.io.fits as pf
import numpy as np
import sys
import pdb


def create_merge_example(x, y, hdus, path, empty=[]):
    """
    Creates a fit file which will store random data inside a number of hdus

    Parameters:
    -----------
    x, y: int
        Size of the example
    hdus : int
        Number of hdus to fill
    empty : list of int
        Indeces of hdu's which will be generated without data
    """
    # Create primary hdu
    data = np.random.rand(x, y)
    primer = pf.PrimaryHDU(data=data, header=pf.Header())
    hdul = pf.HDUList([primer])

    # Include the rest
    for i in range(hdus):
        if i in empty:
            hdu = pf.ImageHDU(header=pf.Header())
        else:
            data = np.random.rand(x, y)
            hdu = pf.ImageHDU(data=data, header=pf.Header())
        hdul.append(hdu)

    hdul.writeto(path)


def create_random_fit(xy, path, header=pf.Header(), min_val=None, max_val=None):
    """
    Generates normal fit with random data
    """
    if min_val is None and max_val is None:
        data = np.random.rand(xy[0], xy[1])
    else:
        data = np.random.randint(min_val, max_val, size=(xy[0], xy[1]))
    primer = pf.PrimaryHDU(data=data, header=header)
    hdul = pf.HDUList([primer])
    hdul.writeto(path)


def create_empty_fit(name="blank.fits"):
    """
    Creates fit with no data, astrofile._read_fit should return None
    """
    blank = pf.PrimaryHDU()
    hdul = pf.HDUList([blank])
    hdul.writeto(name)
