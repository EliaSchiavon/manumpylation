def shift_arr(input_array: np.ndarray, shift_per_ax: tuple) -> np.ndarray:
  
    """
    A function to shift arrays. 
    
    ## Parameters
    input_array: numpy array,
        the input array you want to shift.
    shift_per_ax: tuple:
        the amount to shift on each axis.
        
    ## Example
     ...
    """

    assert len(shift_per_ax) == input_array.ndim

    return ndimage.shift(input_array, shift_per_ax)
