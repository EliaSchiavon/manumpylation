def crop_array_on_mask(input_imgarr: np.ndarray, input_maskarr: np.ndarray) -> np.ndarray:

    """
    Crop the input_imgarr around the provided binary mask
    """

    assert input_imgarr.shape == input_maskarr.shape

    nz_coords_per_ax = list(map(lambda x: np.unique(x), np.nonzero(input_maskarr)))    
    nz_range_per_ax = tuple(slice(min(nz_coords), max(nz_coords)+1) for nz_coords in nz_coords_per_ax)

    return input_imgarr[nz_range_per_ax]