def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    max_val = max(values)
    min_val = min(values)
    if max_val == min_val:
        return [0] * len(values)
        
    bin_width = (max_val - min_val) / num_bins
    bins = []
    for v in values:
        bin_index = int((v - min_val) / bin_width)
        bin_index = min(bin_index, num_bins - 1)
        bins.append(bin_index)
    return bins
    
    