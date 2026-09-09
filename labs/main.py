def unmatched_skus(warehouse_a, warehouse_b):
    return warehouse_a ^ warehouse_b
    # TODO: compute the symmetric difference using union/intersection/difference,
    # without using ^ or .symmetric_difference()
print(unmatched_skus({"A1"}, {"A1"}))