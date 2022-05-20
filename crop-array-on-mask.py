import numpy as np

def crop_array_on_mask(input_arr: np.ndarray, input_maskarr: np.ndarray, margin: tuple = None, margin_perc: tuple = None) -> np.ndarray:

    """
    A function to crop an array on a given mask.

    input_arr: np.ndarray,
        The unmpy array we want to crop around the input mask
    
    input_mask: np.ndarray,
        A binary mask with the same shape of the input array

    margin: tuple,
        Margin in pixels to keep around the mask. 
        If 2 values are specified the first value is intended for row margin and
        the second value for column margin.
    
    margin_perc: tuple,
       Percentage of margin (expressed as a decimal number) to keep around the mask with respect
       to the mask shape.
       If margin is specified this parameter  will be ignored.
       If 2 values are specified the first value is intended for row margin and
       the second value for column margin.
    """

    assert input_arr.shape == input_maskarr.shape, "input_arr and input_mask must have the same shape"

    nz_coords_per_ax = list(map(lambda x: np.unique(x), np.nonzero(input_maskarr)))
    

    if margin is not None:
        margin = margin
    elif margin_perc is not None:
        if margin_perc>1. or margin_perc<0.:
            print("margin_perc should be in the range [0,1]")
            return
        margin = tuple(int(margin_perc*len(nz_coords)) for nz_coords in nz_coords_per_ax)
    else:
        margin = 0
    
    if isinstance(margin, int):
        margin = (margin, )*input_maskarr.ndim
    elif isinstance(margin, tuple):
        if len(margin) != input_maskarr.ndim:
            print("margin should match the number of axes of the input array!")
            return
    else:
        print("margin should be an int or a tuple matching the number of axes of the input array")
        return

    nz_range_per_ax = tuple()
    for i, (nz_coords, ax_margin) in enumerate(zip(nz_coords_per_ax, margin)):
        start_coord = min(nz_coords)-ax_margin
        end_coord = max(nz_coords)+ax_margin+1
        if start_coord<0 or end_coord>input_maskarr.shape[i]:
            print("invalid margin, ignoring that parameter.")
            nz_range_per_ax = tuple(slice(min(nz_coords), max(nz_coords)+1) for nz_coords in nz_coords_per_ax)
            break
        nz_range_per_ax += (slice(min(nz_coords)-ax_margin, max(nz_coords)+ax_margin+1), )
    

    nz_range_per_ax_tup = tuple((nz_range.start, nz_range.stop) for nz_range in nz_range_per_ax)

    return input_arr[nz_range_per_ax], nz_range_per_ax_tup